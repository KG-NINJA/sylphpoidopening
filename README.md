# Wireframe Demo (PC-8801風)

緑色ワイヤーフレームによるレトロPC風アニメーション環境。  
Google Colab やローカルで動作・録画可能。

## セットアップ

```bash
pip install -r requirements.txt
```

## 実行

通常実行:
```bash
python run_demo.py
```

録画（ffmpegが必要）:
```bash
python run_demo.py --record --width 1280 --height 720
```

Colabで実行例:
```python
!apt-get update && apt-get install -y xvfb ffmpeg
!pip install pygame PyOpenGL
!xvfb-run -s "-screen 0 1280x720x24" python run_demo.py --record --width 1280 --height 720
from IPython.display import Video
Video("demo.mp4", embed=True)
```
