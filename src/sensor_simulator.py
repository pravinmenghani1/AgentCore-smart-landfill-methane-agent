# sensor_simulator.py
import random
import time

class SensorSimulator:
    """
    Simulates methane readings over time.
    Generates normal base levels and occasional spikes.
    """
    def __init__(self, base_ppm=800, spike_chance=0.05, max_spike=3000):
        self.base_ppm = base_ppm
        self.spike_chance = spike_chance
        self.max_spike = max_spike

    def stream(self):
        """
        Generator yielding simulated methane readings.
        Each reading is a dict: {"timestamp": ..., "ppm": ...}
        """
        while True:
            reading = self.generate_reading()
            yield reading
            time.sleep(1)

    def generate_reading(self):
        spike = self.max_spike if random.random() < self.spike_chance else 0
        ppm = self.base_ppm + random.randint(-50, 50) + spike
        return {"timestamp": time.time(), "ppm": ppm}
