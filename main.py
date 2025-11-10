import argparse

from drums import DrumMachine

def parse():
    """Parse command-line arguments for the drum machine."""
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
        type=int,
        default=4,
        help="Bars per phrase (default: 4)",
    )
    parser.add_argument(
        "--time",
        type=str,
        default="4/4",
        help="Time signature (default: 4/4, e.g. 3/4)",
    )
    args = parser.parse_args()
    try:
        beats, note_value = map(int, args.time.split("/"))
    except ValueError:
        raise ValueError("Invalid time signature format. Use e.g. 3/4 or 4/4")
    args.time_signature = (beats, note_value)
    return args

def main():
    args = parse()
    dm = DrumMachine(bpm=args.bpm, time_signature=args.time_signature)
    dm.load_samples(args.config)
    dm.loop(args.bars)

if __name__ == "__main__":
    main()
