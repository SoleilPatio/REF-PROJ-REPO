# Information
  - [perfetto github](https://github.com/google/perfetto)
  - [perfetto document](https://perfetto.dev/docs/)

# Build Commands
## Build UI
  - [UI development](https://perfetto.dev/docs/contributing/ui-getting-started)
  - [編譯步驟]
    - [build tool]()
      ```sh
      tools/install-build-deps --android --ui --linux-arm
      tools/gn args out/linux   #only android need to write config file
      tools/ninja -C out/linux
      ```
    - [build ui]()
      ```sh
      git config --global safe.directory '*'  #[optional] NFS問題1: git檢查nfs磁碟權限跟owner不一樣
      tools/install-build-deps --ui
      tools/gn clean <output_directory>       #[optional] avoid stale binary files.

      # Will build into ./out/ui by default. Can be changed with --out path/
      # The final bundle will be available at ./ui/out/dist/.
      # The build script creates a symlink from ./ui/out to $OUT_PATH/ui/.
      ui/build
      ```
      - [NFS問題2:emscripten編譯失敗，將cache移動到本機，不要在NFS]
        - 修改 NDK-LinuxNFS\perfetto\perfetto\gn\standalone\.emscripten
          ```python
          # [CLS]
          # Prefer local (non-NFS) cache/temp to avoid NFS locking issues.
          CACHE = os.environ.get('EM_CACHE') or os.path.join(os.path.expanduser('~'), '.cache', 'emscripten')
          TEMP_DIR = os.environ.get('EMCC_TEMP_DIR') or os.path.join(os.path.expanduser('~'), '.cache', 'emscripten_tmp')
          ```
      - [執行]
        - ui/run-dev-server
      - [打包一個給別人local使用的UI]
        ```sh
        cd ui
        npm run build
        # 產物都在 out/ui/ui/dist 底下,找有index.html的地方啓動web server
        python3 -m http.server 8080                 # local 使用
        python3 -m http.server 10000 --bind 0.0.0.0 # 別人用 http://你的本機IP:10000 存取

        ```


# Record
  ```sh
  sudo ./perfetto/out/linux/traced &
  sudo ./perfetto/out/linux/traced_probes &
  sudo ./perfetto/out/linux/perfetto --txt -c perfetto.config -o trace.ptrace
  ```


