# planner_agent.py
from config import METHANE_THRESHOLD_PPM, PREDICTION_HORIZON_HOURS

class PlannerAgent:
    """
    Predictive agent that decides whether vent/flare is needed.
    Currently uses simple heuristic: if current or predicted ppm exceeds threshold.
    """
    def __init__(self):
        self.recent_readings = []

    def evaluate(self, reading):
        self.recent_readings.append(reading)
        if len(self.recent_readings) > 10:
            self.recent_readings.pop(0)

        predicted_ppm = self.predict_next_ppm()
        action_needed = predicted_ppm >= METHANE_THRESHOLD_PPM

        plan = {
            "timestamp": reading["timestamp"],
            "current_ppm": reading["ppm"],
            "predicted_ppm": predicted_ppm,
            "action_needed": action_needed,
            "action_type": "VENT_FLARE" if action_needed else "NONE"
        }
        return plan

    def predict_next_ppm(self):
        """
        Simple predictive logic: average of last 5 readings + small growth
        """
        if not self.recent_readings:
            return 0
        last_values = [r["ppm"] for r in self.recent_readings[-5:]]
        avg = sum(last_values)/len(last_values)
        growth_factor = 1.05  # assume small increase
        return avg * growth_factor
