# test_sensor_simulator.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from sensor_simulator import SensorSimulator

def test_sensor_reading_format():
    sensor = SensorSimulator()
    reading = sensor.generate_reading()
    
    assert "timestamp" in reading
    assert "ppm" in reading
    assert isinstance(reading["ppm"], (int, float))
    assert reading["ppm"] > 0

def test_sensor_base_levels():
    sensor = SensorSimulator(base_ppm=1000, spike_chance=0)
    reading = sensor.generate_reading()
    
    # Should be around base level (±50)
    assert 950 <= reading["ppm"] <= 1050
