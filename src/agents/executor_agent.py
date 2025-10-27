# executor_agent.py
import os
import json
from config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

class ExecutorAgent:
    """
    Executes the plan (simulated: logs action to file)
    """
    def execute(self, plan):
        if plan["action_needed"]:
            filename = os.path.join(LOG_DIR, f"{int(plan['timestamp'])}_action.json")
            with open(filename, "w") as f:
                json.dump(plan, f, indent=2)
            print(f"[EXECUTOR] Action logged: {plan['action_type']} at ppm={plan['current_ppm']}")
        return plan
