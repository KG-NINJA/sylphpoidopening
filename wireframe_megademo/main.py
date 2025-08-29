import argparse  #KGNINJA
import shutil  #KGNINJA
import subprocess  #KGNINJA
from . import config, renderer, mock  #KGNINJA

def main():  #KGNINJA
    parser = argparse.ArgumentParser()  #KGNINJA
    parser.add_argument("--grid", action="store_true")  #KGNINJA
    parser.add_argument("--record-mock", action="store_true")  #KGNINJA
    parser.add_argument("--fps", type=int, default=config.MOCK_FRAME_RATE)  #KGNINJA
    parser.add_argument("--duration", type=int, default=config.DEMO_TOTAL)  #KGNINJA
    parser.add_argument("--width", type=int, default=640)  #KGNINJA
    parser.add_argument("--height", type=int, default=480)  #KGNINJA
    parser.add_argument("--mock", action="store_true")  #KGNINJA
    args = parser.parse_args()  #KGNINJA

    if args.record_mock:  #KGNINJA
        total_frames = args.duration  #KGNINJA
        mock.render_mock_sequence(args.width, args.height, total_frames, args.fps, grid=args.grid)  #KGNINJA
        if shutil.which("ffmpeg"):  #KGNINJA
            try:  #KGNINJA
                subprocess.run([
                    "ffmpeg", "-y", "-framerate", str(args.fps), "-i", "frames/frame_%04d.png", "demo_mock.mp4"
                ], check=True)  #KGNINJA
            except Exception as e:  #KGNINJA
                print(f"ffmpeg failed: {e}")  #KGNINJA
        else:  #KGNINJA
            print("ffmpeg not found; frames left in frames/")  #KGNINJA
        return  #KGNINJA

    r = renderer.Renderer(args.width, args.height)  #KGNINJA
    timeline = range(args.duration)  #KGNINJA
    r.run(timeline, force_mock=args.mock, grid=args.grid)  #KGNINJA

if __name__ == "__main__":  #KGNINJA
    main()  #KGNINJA
