import argparse

from drums import DrumMachine

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Drum Machine")
    parser.add_argument(
        "--bpm", type=int, default=100, help="Beats per minute (default: 100)"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="Sample config file (default: config.json)",
    )
    parser.add_argument(
        "--bars",
        type=str,
        default=4,
        help="Bars per phrase (default: 4)",
    )
    args = parser.parse_args()
    dm = DrumMachine(bpm=args.bpm)
    dm.load_samples(args.config)
    dm.loop(args.bars)
