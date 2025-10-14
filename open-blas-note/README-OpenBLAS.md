1. 任何使用 OpenBLAS 的程式（如 AnTuTu）在啟動時，libopenblas.so 函式庫會被載入到記憶體。
2. 這個初始化函式會呼叫 getarch() 和 get_cpu_features() 之類的內部函式，最終會執行到 `cpuid_arm64.c` 這個檔案中的程式碼。
3. 真假？  對於 CME，它會檢查 ID_AA64ISAR1_EL1 這個暫存器。該暫存器的第 8 到 11 位元 (ID_AA64ISAR1_EL1[11:8]) 用於表示對複數運算的支援程度。如果值不為 0，就表示 CPU 至少有部分支援。
4. CME 是 ARMv9.2-A 的可選功能，它建立在 SME (Scalable Matrix Extension)  家族之上。因此，程式碼中更有可能檢查的是 SME 或相關的硬體能力（HWCAP）旗標。
5. 相關的偵測邏輯主要在 driver/others/dynamic_arm64.c
6.  偵測功能由一個名為 support_sme1 的函式實現。以下是該函式的核心內容：

    1 #ifndef HWCAP2_SME
    2 #define HWCAP2_SME 1<<23
    3 #endif
    4 
    5 ...
    6 
    7 int support_sme1(void) {
    8         int ret = 0;
    9 
   10 #if (defined OS_LINUX || defined OS_ANDROID)
   11         ret = getauxval(AT_HWCAP2) & HWCAP2_SME;
   12         if(getauxval(AT_HWCAP2) & HWCAP2_SME){
   13                 ret = 1;
   14         }
   15 #endif
   16 #if defined(__APPLE__)
   17   sysctlbyname"hw.optional.arm.FEAT_SME",&value64,&length64,NULL,0);
   18   ret = value64;
   19 #endif
   20        return ret;
   21 }

  運作方式解說

   1. `#if (defined OS_LINUX || defined OS_ANDROID)`: 這段程式碼確保只在 Linux 或 Android 系統上編譯和執行。
   2. `getauxval(AT_HWCAP2)`: 這是整個偵測的核心。getauxval 是 Linux 系統上的一個標準函式，用於從 ELF 輔助向量 (Auxiliary Vector) 中取得 CPU 的硬體資訊。AT_HWCAP2 參數代表它要去查詢「第二組硬體能力標誌」。
   3. `& HWCAP2_SME`: getauxval 返回一個整數，其中每一個位元 (bit) 代表一個特定的硬體功能。程式碼將這個返回值與 HWCAP2_SME 進行「位元 AND 運算」。HWCAP2_SME 是一個常數（位元遮罩，其值為 1<<23），代表 SME 功能對應的位元。
   4. 判斷結果: 如果 CPU 支援 SME，那麼 AT_HWCAP2 中對應 HWCAP2_SME 的位元會被設為 1。進行 AND 運算後的結果就會是一個非零值，函式最終返回 1，表示「支援」。如果不支援，結果為 0，函式返回 0。

  總結來說，OpenBLAS (以及很可能安兔兔) 是透過呼叫 `getauxval(AT_HWCAP2)` 並檢查返回的位元標誌中是否包含 `HWCAP2_SME` 來判斷平台是否支援 ARM SME/CME 的。 這是在 Android/Linux 環境下偵測 CPU 功能的標準且最高效的方法。


  1. OpenBLAS 在哪裡根據 support_sme1 的結果來決定實作？

  這個決策過程主要發生在 OpenBLAS 函式庫初始化的時候，具體來說是在 driver/others/dynamic_arm64.c 檔案的 get_coretype() 函式中。

  當您的程式第一次呼叫 OpenBLAS 的功能時，OpenBLAS 會執行一個名為 gotoblas_dynamic_init() 的初始化函式。這個函式會呼叫 get_coretype() 來偵測當前的
  CPU 型號與特性，並根據結果設定一個名為 gotoblas 的全域指標。這個指標指向一個結構，裡面包含了所有 BLAS 運算（如矩陣乘法 gemm）的函式指標。

  get_coretype() 在快結束的地方有這段關鍵程式碼：

    1 // (位於 driver/others/dynamic_arm64.c 的 get_coretype 函式中)
    2 
    3   ... // 前面是根據 CPU ID 判斷各種 ARM 核心的邏輯
    4 
    5 #if !defined(NO_SME)
    6   if (support_sme1()) {
    7     return &gotoblas_ARMV9SME;
    8   }
    9 #endif
   10 
   11 #ifndef NO_SVE
   12   if ((getauxval(AT_HWCAP) & HWCAP_SVE)) {
   13     return &gotoblas_ARMV8SVE;
   14   }
   15 #endif
   16 
   17   return NULL;

  解說：
   * 程式在判斷完所有已知的 CPU 型號後，會做最後的特性檢查。
   * 它會呼叫 support_sme1()。
   * 如果 support_sme1() 返回 true (非零值)，get_coretype() 就會返回 &gotoblas_ARMV9SME。
   * gotoblas_ARMV9SME 是一個包含了針對 SME 指令集最佳化的函式實作的集合。這個位址會被存到全域的 gotoblas 指標中。
   * 如果 support_sme1() 返回 false，它會繼續往下檢查是否支援 SVE，或者最終返回一個通用的實作。

  結論： 判斷發生在函式庫載入時的初始化階段。一旦 gotoblas 指標被設定為指向 gotoblas_ARMV9SME，之後所有矩陣運算都會自動「分派」到 SME
  的最佳化版本，直到程式結束。

  ---

  2. 如果動態改變 getauxval 的值，是否會讓 OpenBLAS 行為改變？

  關於第二個問題，答案是：不會。

  原因：
  如上所述，getauxval 的呼叫只發生在 gotoblas_dynamic_init() 這個一次性的初始化過程中。

  gotoblas_dynamic_init() 函式的開頭有這樣的保護機制：

   1 void gotoblas_dynamic_init(void) {
   2 
   3   if (gotoblas) return; // 如果已經初始化過了，就直接返回
   4 
   5   // ... 後續的 get_coretype() 和初始化邏輯 ...
   6 }

  這意味著：
   1. 當您的應用程式第一次使用 OpenBLAS 時，gotoblas 是 NULL，初始化程式會執行，呼叫 get_coretype() -> support_sme1() ->
      getauxval()，並根據結果快取（cache）住最佳的函式實作 (gotoblas 指標被賦值)。
   2. 之後您的應用程式每一次呼叫 OpenBLAS 的運算，它都會直接使用 gotoblas 指標中快取的函式位址，並不會重新去呼叫 `getauxval` 做硬體檢查。

  這種「一次檢查，永久使用」的設計是為了效能考量，避免了每次函式呼叫都進行系統呼叫的額外開銷。

  所以，如果您想透過改變 getauxval 的值來影響 OpenBLAS 的行為，您必須設法在 gotoblas_dynamic_init() 首次被執行之前就完成對 getauxval 的掛鉤 (hook)
  或修改。一旦初始化完成，再做任何改變都為時已晚。