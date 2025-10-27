# evidence_agent.py
import os
import json
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from agentcore import BaseAgent, Message
from strands_sdk import DocumentEngine
from config import EVIDENCE_DIR

os.makedirs(EVIDENCE_DIR, exist_ok=True)

class EvidenceAgent(BaseAgent):
    """
    AgentCore-powered compliance evidence generation agent
    """
    def __init__(self, agent_id="evidence_agent"):
        super().__init__(agent_id)
        self.doc_engine = DocumentEngine()
        
    async def process_message(self, message: Message):
        """Generate evidence for executed actions"""
        if message.type == "action_executed":
            return await self.generate_evidence(message.data)
        return None
    
    async def generate_evidence(self, action_data):
        """Generate compliance evidence using Strands document engine"""
        timestamp_str = datetime.fromtimestamp(action_data["timestamp"]).strftime("%Y%m%d_%H%M%S")
        
        # Use Strands document engine for enhanced evidence generation
        evidence_data = await self.doc_engine.generate_compliance_report({
            "action_data": action_data,
            "timestamp": timestamp_str,
            "regulatory_framework": "EPA_METHANE_2024"
        })
        
        pdf_file = os.path.join(EVIDENCE_DIR, f"{timestamp_str}_evidence.pdf")
        json_file = os.path.join(EVIDENCE_DIR, f"{timestamp_str}_evidence.json")

        # Write enhanced JSON with Strands metadata
        with open(json_file, "w") as f:
            json.dump(evidence_data, f, indent=2)

        # Generate enhanced PDF with Strands formatting
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(50, 750, "Smart Landfill Methane Action Evidence")
        c.drawString(50, 730, f"Timestamp: {timestamp_str}")
        c.drawString(50, 710, f"Current PPM: {action_data['current_ppm']}")
        c.drawString(50, 690, f"Predicted PPM: {action_data['predicted_ppm']}")
        c.drawString(50, 670, f"Action: {action_data['action_type']}")
        c.drawString(50, 650, f"Confidence: {action_data.get('confidence', 'N/A')}")
        c.drawString(50, 630, f"Agent ID: {action_data.get('agent_id', 'N/A')}")
        c.drawString(50, 610, f"Reasoning: {action_data.get('reasoning', 'N/A')}")
        c.save()

        print(f"[EVIDENCE] Enhanced PDF + JSON generated: {pdf_file}")
        
        return Message(
            type="evidence_generated",
            data={"pdf_file": pdf_file, "json_file": json_file, "evidence_data": evidence_data},
            sender=self.agent_id
        )
