import json
import math
import random

class DrumMachine:
    def __init__(self, bpm=100, swing=0.0, time_signature=(4,4)):
        self.bpm = bpm
        self.swing = swing
        self.time_signature = time_signature
        self.samples = {}

    def load_samples(self, config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        self.samples = config

    def make_pattern(self):
        beats, note_value = self.time_signature
        steps_per_beat = 4
        steps_per_bar = beats * steps_per_beat
        pattern = []
        for i in range(steps_per_bar):
            step = {
                "kick": random.random() < 0.3,
                "snare": (i % 8 == 4) or random.random() < 0.1,
                "hihat": random.random() < 0.7,
                "crash": (i == 0),
            }
            pattern.append(step)
        return pattern

    def get_config(self):
        return {
            "bpm": self.bpm,
            "swing": self.swing,
            "time_signature": self.time_signature,
            "samples": self.samples
        }
