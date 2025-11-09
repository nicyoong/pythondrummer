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


