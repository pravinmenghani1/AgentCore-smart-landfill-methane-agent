# main.py
from sensor_simulator import SensorSimulator
from agents.planner_agent import PlannerAgent
from agents.safety_guard import SafetyGuard
from agents.executor_agent import ExecutorAgent
from agents.evidence_agent import EvidenceAgent
import time

sensor_sim = SensorSimulator()
planner = PlannerAgent()
guard = SafetyGuard()
executor = ExecutorAgent()
evidence = EvidenceAgent()

print("[SYSTEM] Smart Landfill Methane Capture Agent started (simulation)")

try:
    for reading in sensor_sim.stream():
        plan = planner.evaluate(reading)
        if guard.validate(plan):
            action_log = executor.execute(plan)
            evidence.record(action_log)
        else:
            print(f"[GUARD] Plan invalid for reading {reading['ppm']} ppm")
        time.sleep(0.5)  # speed control
except KeyboardInterrupt:
    print("[SYSTEM] Simulation stopped by user")
