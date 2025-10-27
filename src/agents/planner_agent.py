# planner_agent.py
from strands_sdk import Agent, ReasoningEngine, Task
from agentcore import BaseAgent, Message
from config import METHANE_THRESHOLD_PPM, PREDICTION_HORIZON_HOURS
import asyncio

class PlannerAgent(BaseAgent):
    """
    Strands-powered predictive agent for methane risk assessment
    """
    def __init__(self, agent_id="planner_agent"):
        super().__init__(agent_id)
        self.reasoning_engine = ReasoningEngine()
        self.recent_readings = []
        
    async def process_message(self, message: Message):
        """Process incoming sensor readings using Strands reasoning"""
        if message.type == "sensor_reading":
            return await self.evaluate_reading(message.data)
        return None
    
    async def evaluate_reading(self, reading):
        """Evaluate methane reading using Strands reasoning engine"""
        self.recent_readings.append(reading)
        if len(self.recent_readings) > 10:
            self.recent_readings.pop(0)
        
        # Create Strands task for prediction
        task = Task(
            name="methane_prediction",
            context={
                "current_reading": reading,
                "historical_data": self.recent_readings,
                "threshold": METHANE_THRESHOLD_PPM,
                "horizon_hours": PREDICTION_HORIZON_HOURS
            }
        )
        
        # Use Strands reasoning engine
        result = await self.reasoning_engine.execute(task)
        predicted_ppm = result.get("predicted_ppm", reading["ppm"])
        
        action_needed = predicted_ppm >= METHANE_THRESHOLD_PPM
        
        plan = {
            "timestamp": reading["timestamp"],
            "current_ppm": reading["ppm"],
            "predicted_ppm": predicted_ppm,
            "action_needed": action_needed,
            "action_type": "VENT_FLARE" if action_needed else "NONE",
            "confidence": result.get("confidence", 0.8),
            "reasoning": result.get("explanation", "Threshold-based decision")
        }
        
        return Message(type="action_plan", data=plan, sender=self.agent_id)
