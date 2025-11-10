import json
import time
import pygame
import random

pygame.mixer.init()
pygame.init()


class DrumMachine:
    def __init__(self, bpm=100, time_signature=(4, 4)):
        self.bpm = bpm
        self.time_signature = time_signature  # e.g., (3, 4) or (4, 4)
        self.beat_duration = 60 / bpm
        self.samples = {}
        self.playing = True
        self.screen = pygame.display.set_mode((300, 100))
        pygame.display.set_caption("Drum Machine")
        self.draw_status()

    def draw_status(self):
        """Draws play/pause status and basic visuals."""
        self.screen.fill((20, 20, 20))  # dark background
        font = pygame.font.SysFont("Verdana", 36, bold=True)

        # Choose icon and color
        if self.playing:
            text = font.render("PLAYING", True, (0, 255, 0))
        else:
            text = font.render("PAUSED", True, (255, 255, 0))

        rect = text.get_rect(center=(150, 50))
        self.screen.blit(text, rect)

        pygame.display.flip()

    def load_samples(self, config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        self.samples["kick"] = pygame.mixer.Sound(config["kick"])
        self.samples["snare"] = pygame.mixer.Sound(config["snare"])
        self.samples["hihat"] = pygame.mixer.Sound(config["hihat"])
        self.samples["crash"] = pygame.mixer.Sound(config["crash"])

    def make_pattern(self):
        beats, note_value = self.time_signature
        steps_per_beat = 4
        steps_per_bar = beats * steps_per_beat
        snare_div = 8 if beats == 4 else 12
        pattern = []
        for i in range(steps_per_bar):
            step = {
                "kick": random.random() < 0.3,
                "snare": (i % snare_div == 4) or random.random() < 0.1,
                "hihat": random.random() < 0.7,
                "crash": (i == 0),
            }
            if sum(step.values()) > 3:
                candidates = [k for k in step if k != "kick" and step[k]]
                if candidates:
                    mute = random.choice(candidates)
                    step[mute] = False
            pattern.append(step)
        return pattern

    def handle_events(self):
        """Handle key and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playing = not self.playing
                    print("▶️  Resumed" if self.playing else "⏸️  Paused")
                    self.draw_status()

    def play_pattern(self, pattern):
        """Play pattern once."""
        for step in pattern:
            self.handle_events()
            while not self.playing:
                self.handle_events()
                time.sleep(0.05)
            for drum, play in step.items():
                if play:
                    self.samples[drum].play()
            time.sleep(self.beat_duration / 4)
            self.draw_status()

    def loop(self, phrase_length=4):
        pattern = self.make_pattern()
        print(
            f"Playing beat ({phrase_length}-bar phrases), press SPACE to pause/resume, close window or Ctrl+C to quit"
        )
        try:
            bars_played = 0
            while True:
                self.play_pattern(pattern)  # assume this plays 1 bar
                bars_played += 1

                # If we've reached the phrase length, make a new pattern
                # if bars_played % phrase_length == 0 and random.random() < 0.5:
                if bars_played % phrase_length == 0:
                    pattern = self.make_pattern()
        except KeyboardInterrupt:
            print("\nStopped.")
            pygame.quit()
