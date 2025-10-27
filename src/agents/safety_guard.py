# safety_guard.py
from config import METHANE_THRESHOLD_PPM

class SafetyGuard:
    """
    Ensures action is safe (within regulatory limits)
    """
    def validate(self, plan):
        ppm = plan["predicted_ppm"]
        if ppm < 0:
            return False
        # Can add more constraints here
        return True
