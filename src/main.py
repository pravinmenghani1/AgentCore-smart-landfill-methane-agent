# main.py
import asyncio
from agentcore import AgentOrchestrator, Message
from sensor_simulator import SensorSimulator
from agents.planner_agent import PlannerAgent
from agents.safety_guard import SafetyGuard
from agents.executor_agent import ExecutorAgent
from agents.evidence_agent import EvidenceAgent

class MethaneMonitoringSystem:
    """
    AgentCore-orchestrated methane monitoring system
    """
    def __init__(self):
        self.orchestrator = AgentOrchestrator()
        self.sensor_sim = SensorSimulator()
        
        # Initialize agents
        self.planner = PlannerAgent()
        self.guard = SafetyGuard()
        self.executor = ExecutorAgent()
        self.evidence = EvidenceAgent()
        
        # Register agents with orchestrator
        self.orchestrator.register_agent(self.planner)
        self.orchestrator.register_agent(self.guard)
        self.orchestrator.register_agent(self.executor)
        self.orchestrator.register_agent(self.evidence)
        
        # Set up message routing
        self.setup_message_routing()
    
    def setup_message_routing(self):
        """Configure message flow between agents"""
        # Sensor readings -> Planner
        self.orchestrator.add_route("sensor_reading", "planner_agent")
        
        # Action plans -> Safety Guard
        self.orchestrator.add_route("action_plan", "safety_guard")
        
        # Validated plans -> Executor
        self.orchestrator.add_route("validated_plan", "executor_agent")
        
        # Executed actions -> Evidence
        self.orchestrator.add_route("action_executed", "evidence_agent")
    
    async def run(self):
        """Run the monitoring system"""
        print("[SYSTEM] AgentCore Smart Landfill Methane Capture Agent started")
        
        try:
            # Start orchestrator
            await self.orchestrator.start()
            
            # Process sensor readings
            for reading in self.sensor_sim.stream():
                # Send sensor reading to orchestrator
                message = Message(
                    type="sensor_reading",
                    data=reading,
                    sender="sensor_simulator"
                )
                
                await self.orchestrator.process_message(message)
                await asyncio.sleep(0.5)  # Control simulation speed
                
        except KeyboardInterrupt:
            print("[SYSTEM] Simulation stopped by user")
        finally:
            await self.orchestrator.stop()

async def main():
    """Main entry point"""
    system = MethaneMonitoringSystem()
    await system.run()

if __name__ == "__main__":
    asyncio.run(main())
