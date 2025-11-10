# Simple Drum Machine

A basic drum machine written in Python using Pygame. It generates random 16-step drum patterns and allows play/pause control in real time.

## Features
- Randomized drum patterns
- Supports kick, snare, hi-hat, and crash sounds
- Adjustable tempo (BPM)
- Pause/resume with the spacebar
- Simple visual indicator for play/pause

## Requirements
- Python 3.8 or higher
- Pygame library

Install dependencies:
```bash
pip install pygame
```

## Configuration

Create a `config.json` file that defines the paths to your audio samples:

```
{
    "kick": "samples/kick.wav",
    "snare": "samples/snare.wav",
    "hihat": "samples/hihat.wav",
    "crash": "samples/crash.wav"
}
```

## Usage

Run the program from the command line:

```
python drums.py --bpm 120 --config config.json
```

## Command line options

| Option     | Description                  | Default     |
| ---------- | ---------------------------- | ----------- |
| `--bpm`    | Beats per minute             | 100         |
| `--config` | Path to sample configuration | config.json |

## Controls

| Key                    | Action                |
| ---------------------- | --------------------- |
| Spacebar               | Pause/Resume playback |
| Close window or Ctrl+C | Quit the program      |