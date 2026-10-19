from fastapi import FastAPI
from typing import List
from models.schemas import FarmerProfile, PolicyDelta
from services.matchmaker import find_affected_farmers
from services.notification import generate_voice_dispatch

app = FastAPI(title="Proactive Policy Delta Engine")

# Mock Farmer Database (AgriStack Compatible format)
MOCK_FARMERS: List[FarmerProfile] = [
    FarmerProfile(
        farmer_id="FARM-001",
        name="Ramesh Patil",
        state="Maharashtra",
        district="Nashik",
        land_holding_hectares=1.5,
        crops_grown=["Soybean", "Onion"],
        social_category="OBC",
        phone_number="+919876543210",
        preferred_language="mr"
    ),
    FarmerProfile(
        farmer_id="FARM-002",
        name="Harpreet Singh",
        state="Punjab",
        district="Ludhiana",
        land_holding_hectares=4.5,
        crops_grown=["Wheat"],
        social_category="General",
        phone_number="+919876543211",
        preferred_language="pa"
    )
]

@app.get("/")
def home():
    return {"message": "Policy Delta Engine backend is active"}

@app.post("/api/v1/trigger-delta-alert")
def trigger_delta_alert(delta: PolicyDelta):
    # Step 1: Filter affected farmers only
    affected_farmers = find_affected_farmers(delta, MOCK_FARMERS)
    
    # Step 2: Generate personalized audio/action guidance
    alerts = [generate_voice_dispatch(farmer, delta) for farmer in affected_farmers]
    
    return {
        "success": True,
        "policy_update": delta.scheme_name,
        "total_affected_farmers": len(affected_farmers),
        "dispatched_alerts": alerts
    }
