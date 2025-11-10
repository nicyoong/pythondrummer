import json
import time
import pygame
import random

pygame.mixer.init()
pygame.init()


class DrumMachine:
    def __init__(self, bpm=100):
        self.bpm = bpm
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
        pattern = []
        for i in range(16):
            step = {
                "kick": random.random() < 0.3,
                "snare": (i % 8 == 4) or random.random() < 0.1,
                "hihat": random.random() < 0.7,
                "crash": (i == 0),
            }
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

    def loop(self):
        pattern = self.make_pattern()
        print(
            "Playing beat, press SPACE to pause/resume, close window or Ctrl+C to quit"
        )
        try:
            while True:
                self.play_pattern(pattern)
                if random.random() < 0.2:
                    pattern = self.make_pattern()
        except KeyboardInterrupt:
            print("\nStopped.")
            pygame.quit()
