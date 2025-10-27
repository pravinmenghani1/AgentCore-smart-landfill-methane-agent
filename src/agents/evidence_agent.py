# evidence_agent.py
import os
import json
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from config import EVIDENCE_DIR

os.makedirs(EVIDENCE_DIR, exist_ok=True)

class EvidenceAgent:
    """
    Generates compliance evidence in PDF + JSON
    """
    def record(self, plan):
        timestamp_str = datetime.fromtimestamp(plan["timestamp"]).strftime("%Y%m%d_%H%M%S")
        pdf_file = os.path.join(EVIDENCE_DIR, f"{timestamp_str}_evidence.pdf")
        json_file = os.path.join(EVIDENCE_DIR, f"{timestamp_str}_evidence.json")

        # Write JSON
        with open(json_file, "w") as f:
            json.dump(plan, f, indent=2)

        # Write PDF
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(50, 750, f"Smart Landfill Methane Action Evidence")
        c.drawString(50, 730, f"Timestamp: {timestamp_str}")
        c.drawString(50, 710, f"Current PPM: {plan['current_ppm']}")
        c.drawString(50, 690, f"Predicted PPM: {plan['predicted_ppm']}")
        c.drawString(50, 670, f"Action: {plan['action_type']}")
        c.save()

        print(f"[EVIDENCE] PDF + JSON generated: {pdf_file}")
