import time
import random
import simpleaudio as sa

class DrumMachine:
    def __init__(self, bpm=100):
        self.bpm = bpm
        self.beat_duration = 60 / bpm
        self.samples = {}


