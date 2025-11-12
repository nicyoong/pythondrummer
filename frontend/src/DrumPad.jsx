import { useState, useEffect } from "react";

export default function DrumPad({ pattern, samples, bpm }) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);

  const playSample = (url) => {
    const audio = new Audio(url);
    audio.currentTime = 0;
    audio.play();
  };

  useEffect(() => {
    if (!isPlaying || !pattern.length) return;

    const stepTime = (60 / bpm) / 4 * 1000; // ms per 16th
    const interval = setInterval(() => {
      const step = pattern[currentStep];
      Object.keys(step).forEach(drum => {
        if (step[drum]) playSample(samples[drum]);
      });
      setCurrentStep((s) => (s + 1) % pattern.length);
    }, stepTime);

    return () => clearInterval(interval);
  }, [isPlaying, currentStep, pattern, samples, bpm]);

  return (
    <div className="drum-pad">
      <h3>Pattern Player</h3>
      <button onClick={() => setIsPlaying(!isPlaying)}>
        {isPlaying ? "⏸ Pause" : "▶️ Play"}
      </button>
      <p>Step: {currentStep + 1}/{pattern.length}</p>
    </div>
  );
}
