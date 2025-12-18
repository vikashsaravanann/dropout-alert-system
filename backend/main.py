from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class StudentRisk(BaseModel):
    student_id: str
    risk_score: float
    top_risk_factors: List[str] # e.g.,
    location_lat: float
    location_long: float

@app.post("/sync/upload_risk_data")
async def sync_risk_data(risks: List):
    """
    Receives offline-calculated risk scores when the teacher connects to internet.
    Triggers CSR alerts if specific thresholds are met.
    """
    blossom_bus_alerts =
    infra_alerts =

    for r in risks:
        # Save to Central DB (Pseudocode)
        # db.save(r)
        
        # Logic: If Risk is High AND Factor is Distance -> Flag for Bus
        if r.risk_score > 0.8 and "Distance" in r.top_risk_factors:
            blossom_bus_alerts.append(r)
        
        # Logic: If Risk is High AND Factor is Sanitation -> Flag for Repair
        if r.risk_score > 0.7 and "Sanitation" in r.top_risk_factors:
            infra_alerts.append(r)

    return {
        "status": "synced", 
        "csr_actions": {
            "bus_route_optimizations_needed": len(blossom_bus_alerts),
            "infra_tickets_raised": len(infra_alerts)
        }
    }
