# safety_guard.py
from agentcore import BaseAgent, Message
from strands_sdk import ValidationEngine
from config import METHANE_THRESHOLD_PPM

class SafetyGuard(BaseAgent):
    """
    AgentCore-powered safety validation agent
    """
    def __init__(self, agent_id="safety_guard"):
        super().__init__(agent_id)
        self.validator = ValidationEngine()
        
    async def process_message(self, message: Message):
        """Validate action plans for safety compliance"""
        if message.type == "action_plan":
            return await self.validate_plan(message.data)
        return None
    
    async def validate_plan(self, plan):
        """Validate plan using Strands validation engine"""
        validation_rules = {
            "ppm_range": {"min": 0, "max": 10000},
            "confidence_threshold": 0.6,
            "regulatory_limits": {"max_ppm": METHANE_THRESHOLD_PPM * 2}
        }
        
        result = await self.validator.validate(plan, validation_rules)
        
        is_valid = (
            plan["predicted_ppm"] >= 0 and
            plan.get("confidence", 0) >= validation_rules["confidence_threshold"] and
            result.get("compliant", True)
        )
        
        validation_result = {
            "plan": plan,
            "valid": is_valid,
            "validation_details": result,
            "timestamp": plan["timestamp"]
        }
        
        return Message(
            type="validated_plan" if is_valid else "invalid_plan",
            data=validation_result,
            sender=self.agent_id
        )
