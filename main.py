from drums import DrumMachine

if __name__ == "__main__":
    dm = DrumMachine(bpm=100)
    dm.load_samples("kick.wav", "snare.wav", "hihat.wav")
    dm.loop()
