# test_agents.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from agents.planner_agent import PlannerAgent
from agents.safety_guard import SafetyGuard
import time

def test_planner_evaluation():
    planner = PlannerAgent()
    reading = {"timestamp": time.time(), "ppm": 2000}
    
    plan = planner.evaluate(reading)
    
    assert "timestamp" in plan
    assert "current_ppm" in plan
    assert "predicted_ppm" in plan
    assert "action_needed" in plan
    assert "action_type" in plan

def test_safety_guard_validation():
    guard = SafetyGuard()
    valid_plan = {"predicted_ppm": 1600}
    invalid_plan = {"predicted_ppm": -100}
    
    assert guard.validate(valid_plan) == True
    assert guard.validate(invalid_plan) == False
