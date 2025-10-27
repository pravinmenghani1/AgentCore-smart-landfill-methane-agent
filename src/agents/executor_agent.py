# executor_agent.py
import os
import json
from agentcore import BaseAgent, Message
from strands_sdk import ActionEngine
from config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

class ExecutorAgent(BaseAgent):
    """
    AgentCore-powered action execution agent
    """
    def __init__(self, agent_id="executor_agent"):
        super().__init__(agent_id)
        self.action_engine = ActionEngine()
        
    async def process_message(self, message: Message):
        """Execute validated action plans"""
        if message.type == "validated_plan":
            return await self.execute_plan(message.data["plan"])
        return None
    
    async def execute_plan(self, plan):
        """Execute action using Strands action engine"""
        if plan["action_needed"]:
            # Use Strands action engine for execution
            execution_result = await self.action_engine.execute({
                "action_type": plan["action_type"],
                "parameters": {
                    "ppm_level": plan["current_ppm"],
                    "predicted_ppm": plan["predicted_ppm"],
                    "timestamp": plan["timestamp"]
                }
            })
            
            # Log action
            filename = os.path.join(LOG_DIR, f"{int(plan['timestamp'])}_action.json")
            log_data = {
                **plan,
                "execution_result": execution_result,
                "agent_id": self.agent_id
            }
            
            with open(filename, "w") as f:
                json.dump(log_data, f, indent=2)
                
            print(f"[EXECUTOR] Action executed: {plan['action_type']} at ppm={plan['current_ppm']}")
            
            return Message(
                type="action_executed",
                data=log_data,
                sender=self.agent_id
            )
        
        return Message(
            type="no_action_needed",
            data=plan,
            sender=self.agent_id
        )
