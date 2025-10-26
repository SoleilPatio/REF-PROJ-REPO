[repo](https://github.com/comfyanonymous/ComfyUI)

# [Manual Install]()
1. python -> 3.13 
   1. py -3.13 -m venv .venv-win-3.13
   2. .\.venv-win-3.13\Scripts\activate.bat
2. git clone https://github.com/comfyanonymous/ComfyUI.git
3. NVIDIA
   - 要安裝torch (要對應 python版本-pyttorch版本-cuda版本)
   - pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
4. pip install -r requirements.txt
5. python main.py

# [Launch BAT]()
@echo off
set ROOT_DIR=C:\APN\PRJ\AI-Vision\ComfyUI\ComfyUI

pushd %ROOT_DIR%
start "" ..\.venv-win-3.13\Scripts\python.exe main.py
timeout /t 5 /nobreak >nul
start "" http://127.0.0.1:8188
popd


# [Plugin]
* [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager)

# [Memo]
  - save image prefix: ComfyUI-%date:yyyyMMdd_hhmmss%
  - save image prefix: video/Wan2.2-%date:yyyyMMdd_hhmmss%
  - save image prefix: ComfyUI-%date:yyyyMMdd_hhmmss%-%KSampler.seed%
  - save image prefix: ComfyUI-%date:yyyyMMdd_hhmmss%-%CLIPTextEncode.text%