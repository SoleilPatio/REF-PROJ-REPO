# install Repo
mkdir ~/bin
PATH=~/bin:$PATH

  - curl sometimes cannot write ome directory, this will failed:
    - curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
  - use this, and move to ~/bin by yourself
    - curl https://storage.googleapis.com/git-repo-downloads/repo -o repo

chmod a+x ~/bin/repo

# repo init
  您可以訪問 [AOSP Build Numbers](https://source.android.com/setup/build-numbers) 頁面來查看所有可用的分支
  --depth=1 可以減少下載量，但若要切換分支或查看完整歷史紀錄，請不要使用此選項
  一般來說，直接下載完整歷史紀錄會更方便
repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r1

repo init -u https://android.googlesource.com/platform/manifest -b android-latest-release --depth=1 ==> 改成這樣

# 同步
repo sync -j$(nproc --all)

# Kernel source
  - 先看AOSP menifest.xml 的 android是什麼版本，再去找對應的核心
  - [找對應的核心](https://android.googlesource.com/kernel/manifest)
  - mkdir gki_kernel
    cd gki_kernel
    repo init -u https://android.googlesource.com/kernel/manifest -b common-android16-6.12
    repo sync -j$(nproc --all)
