1. Scudo 的程式碼在哪裡？
      Scudo 是 LLVM compiler-rt 專案的一部分。在 AOSP 原始碼樹中，它的位置通常在 external/compiler-rt/lib/scudo/。它是一個使用者空間
  (userspace) 的記憶體分配器，因此您不會在 gki_kernel (核心) 目錄中找到它的實作。

2. HybridMutex 是 Scudo 的一部分嗎？在哪裡？
      是的，HybridMutex 是 Scudo 內部使用的一個關鍵類別。它也位於 Scudo 的原始碼目錄內，通常路徑會是
  external/compiler-rt/lib/scudo/common/mutex.h。


從 Android 11 開始，Android 的 Bionic `libc.so` 在建構時，其內部的 `malloc`、`free` 等堆積記憶體管理功能的預設實作就是 Scudo。

  所以，整個關係鏈是這樣的：

   1. Android App (Native Code): 呼叫標準的 malloc() 來申請記憶體。
   2. Bionic C Library (`libc.so`): App 的 malloc() 呼叫被連結到 libc.so。
   3. Scudo Implementation: libc.so 內部的 malloc() 實作，實際上就是呼叫 Scudo 的分配器。


# source code:

## libc.so
aosp-google/aosp-google/bionic/libc/Android.bp

  - 開關scudo
    - 線索: undefined USE_SCUDO, 則會用回jemalloc
    - malloc_low_memory: {   cflags: ["-UUSE_SCUDO"],   whole_static_libs: ["libjemalloc5"]


## libscudo.o
aosp-google/aosp-google/external/scudo/Android.bp

  - libscudo.o 是一個static lib被包在libc.so


### [patch_1][Slow Lock] class CAPABILITY("mutex") HybridMutex ==> 已經有分三階段lock ,最後才是會sleep的slowLock
aosp-google/aosp-google/external/scudo/standalone/mutex.h



### [patch_2][Primary Alolocator] TSDCount增加 => 大家不用lock,不用競爭就可以alloc/free (GB SC+0 , GB MC+79)
aosp-google/aosp-google/external/scudo/standalone/allocator_config.h
  AndroidConfig
     using TSDRegistryT = TSDRegistrySharedT<A, 8U, 2U>; // Shared, max 8 TSDs.
        A -> class Allocator
        8U -> u32 TSDsArraySize
        2U -> u32 DefaultTSDCount
        為 A 類型的分配器，建立一個最多能容納 8 個 TSD 的註冊表，但在執行時，預設會根據 CPU 核心數最多啟用 2 個 TSD。
        TSD雖然叫做Thread Specific Data,但其實是所有thread去共用現有的TSD的，每個TSD有lock(HybridMutex)
        TSD是用來暫時存放user space free的記憶體，每一個TSD有個上限(比如1MB),所以TSD越多會造成佔用系統不還的記憶體越多

### [patch_3][Secondary Allocator] Secondary Backedn的block count & block size ==> (GB SC+5, GB MC+49)
aosp-google/aosp-google/external/scudo/standalone/allocator_config.h
  template <typename Config> using CacheT = MapAllocatorCache<Config>;
        static const u32 DefaultMaxEntriesCount = 32U;      # ==> 256
        static const uptr DefaultMaxEntrySize = 2UL << 20;  # ==> 4UL


  - 主要存放large block (malloc > 64K)
