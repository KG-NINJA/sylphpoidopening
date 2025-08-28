import argparse
from demo.animation import run_animation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=640)
    parser.add_argument("--height", type=int, default=480)
    parser.add_argument("--record", action="store_true")
    args = parser.parse_args()

    run_animation(width=args.width, height=args.height, record=args.record)

if __name__ == "__main__":
    main()
