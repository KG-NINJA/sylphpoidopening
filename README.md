[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KG-NINJA/sylphpoidopening/blob/main/run_demo.ipynb)

# Wireframe Demo (PC-8801風)

Cloud-first, Colab-friendly, GPU-free wireframe animation environment. #KGNINJA

## Intro

緑色ワイヤーフレームによるレトロPC風アニメーション環境。
クラウド利用を前提にし、GPUなしで動作します。

### Cloud Usage

ヘッドレス環境では `xvfb` と `ffmpeg` を使ってレンダリングや録画を行います。

## Setup

```bash
pip install pygame PyOpenGL
sudo apt-get update && sudo apt-get install -y xvfb ffmpeg
```

## Run

Hello app:
```bash
python run_demo.py
```

Megademo:
```bash
python run_megademo.py
```

Wireframe demo with grid (add --mock for log only):
```bash
python run_demo.py --grid
```

## Record

CPU mock recording (fast):
```bash
python run_demo.py --record --fps 10
```

Full recording with xvfb:
```bash
xvfb-run -s "-screen 0 1280x720x24" python run_megademo.py --record-mock
```

## Colab Example

```python
!apt-get update && apt-get install -y xvfb ffmpeg
!pip install pygame PyOpenGL
!python run_demo.py --record --fps 10
from google.colab import files
files.download('demo_mock.mp4')
```

## Policy

事前生成された動画はリポジトリに保存しません。必要に応じて生成してください。
