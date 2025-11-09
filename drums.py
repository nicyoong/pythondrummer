import time
import random
import simpleaudio as sa

class DrumMachine:
    def __init__(self, bpm=100):
        self.bpm = bpm
        self.beat_duration = 60 / bpm
        self.samples = {}

    def load_samples(self, kick_path, snare_path, hihat_path):
        self.samples["kick"] = sa.WaveObject.from_wave_file(kick_path)
        self.samples["snare"] = sa.WaveObject.from_wave_file(snare_path)
        self.samples["hihat"] = sa.WaveObject.from_wave_file(hihat_path)

    def make_pattern(self):
        """Generate a 16-step random drum pattern."""
        pattern = []
        for i in range(16):
            step = {
                "kick": random.random() < 0.3,
                "snare": (i % 8 == 4) or random.random() < 0.1,
                "hihat": random.random() < 0.7
            }
            pattern.append(step)
        return pattern

    def play_pattern(self, pattern):
        """Play the given pattern once."""
        for step in pattern:
            for drum, play in step.items():
                if play:
                    self.samples[drum].play()
            time.sleep(self.beat_duration / 4)  # 16th notes

    def loop(self):
        """Keep generating and playing patterns indefinitely."""
        pattern = self.make_pattern()
        print("Playing beat — press Ctrl+C to stop")

        try:
            while True:
                self.play_pattern(pattern)
                if random.random() < 0.2:  # mutate occasionally
                    pattern = self.make_pattern()
        except KeyboardInterrupt:
            print("\nStopped.")
