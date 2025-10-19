repo: https://github.com/Wan-Video/Wan2.1



# 安裝步驟
1. git clone https://github.com/Wan-Video/Wan2.1.git
2. pip install -r requirements.txt
   1. flash_attn會遇到問題，[參考](#"flash_attn-大魔王-在windows很難裝)
3. download model
   1. pip install "huggingface_hub[cli]"
   2. [14B模型太大會爆跑不動]
      1. huggingface-cli download Wan-AI/Wan2.1-T2V-14B --local-dir ./Wan2.1-T2V-14B
      2. huggingface-cli download Wan-AI/Wan2.1-I2V-14B-720P --local-dir ./Wan2.1-I2V-14B-720P
   3. [只能用1.3B的模型，大概佔VRAM14G]
      1. huggingface-cli download Wan-AI/Wan2.1-T2V-1.3B --local-dir ./Wan2.1-T2V-1.3B    
      2. huggingface-cli download Wan-AI/Wan2.1-I2V-14B-480P --local-dir ./Wan2.1-I2V-14B-480P

# 執行
[失敗]
python generate.py  --task t2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-T2V-14B --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."
python generate.py  --task t2v-14B --size 832*480 --ckpt_dir ./Wan2.1-T2V-14B --offload_model True --t5_cpu --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."
python generate.py  --task t2v-14B --size 640*480 --ckpt_dir ./Wan2.1-T2V-14B --offload_model True --t5_cpu --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."

python generate.py  --task t2v-1.3B --size 832*480 --ckpt_dir ./Wan2.1-T2V-1.3B --offload_model True --t5_cpu --sample_shift 8 --sample_guide_scale 6 --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."

[可以成功]
python generate.py  --task t2v-1.3B --size 480*832 --ckpt_dir ./Wan2.1-T2V-1.3B --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."



# flash_attn 大魔王 在windows很難裝
觀念:
  1. flash_attn 要編譯，必須配合特定的torch , cuda版本. 在windows環境只要一點版本沒對應就會失敗
  2. 安裝windows pre-built的flash_attn ,但是要配合它當時編譯的環境的 torch/cuda版本
  3. torch 會自帶cuda runtime, 所以除非你要自己編譯，不用安裝cuda toolkid，不用管系統的cuda版本(因爲已經決定要用prebuilt flash_attn了)
安裝步驟:
  1. 在這邊找對應python版本的flash_attn prebuilt
     1. [pre-built wheels for windows](https://github.com/mjun0812/flash-attention-prebuild-wheels?utm_source=chatgpt.com)
     2. 有prebuilt : Python 3.12 + CUDA 12.6 + Torch 2.9
  2. [Optional] 安裝對應的cuda toolkit版本可以省略, 因爲torch已經自帶對應版本的cuda runtime了
     1. [google search: cuda 12.6 download](https://developer.nvidia.com/cuda-12-6-0-download-archive)
     2. PyTorch 會附帶 CUDA Runtime（執行時環境） 所以根本不用裝cuda toolkit
  3. 安裝指定版本的torch
     1. python -m pip install torch==2.9.0 --index-url https://download.pytorch.org/whl/cu126
     2. python -m pip install torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126 #安裝其他cu126相容版本
  4. 安裝 flash_attn prebuilt
     1. pip install "C:\Users\cloud\Downloads\flash_attn-2.8.3+cu126torch2.9-cp312-cp312-win_amd64.whl



# 檢查環境
python -c "import sys, platform; print('Python:', sys.version); print('OS:', platform.system(), platform.release())"

    Python: 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
    OS: Windows 10

# 檢查 torch 版本
python -c "import torch, sys; print('Torch:', torch.__version__); print('CUDA:', getattr(torch.version, 'cuda', None)); print('CUDA available:', torch.cuda.is_available()); print('Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"

    Torch: 2.2.1+cu121
    CUDA: 12.1
    CUDA available: True
    Device: NVIDIA GeForce RTX 4090

# 檢查 nvcc 版本
nvcc -V

    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2023 NVIDIA Corporation
    Built on Wed_Feb__8_05:53:42_Coordinated_Universal_Time_2023
    Cuda compilation tools, release 12.1, V12.1.66
    Build cuda_12.1.r12.1/compiler.32415258_0


