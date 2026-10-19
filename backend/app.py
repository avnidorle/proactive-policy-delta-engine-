from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
from models.schemas import FarmerProfile, PolicyDelta
from services.matchmaker import find_affected_farmers
from services.notification import generate_voice_dispatch
import os

app = FastAPI(title="Proactive Policy Delta Engine")

# CORS setup (taaki frontend bina kisi issue ke API call kar sake)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Farmer Database (AgriStack format)
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
    ),
    FarmerProfile(
        farmer_id="FARM-003",
        name="Sunita Devi",
        state="Maharashtra",
        district="Pune",
        land_holding_hectares=0.8,
        crops_grown=["Soybean", "Vegetables"],
        social_category="SC",
        phone_number="+919876543212",
        preferred_language="mr"
    )
]

@app.get("/api/v1/farmers")
def get_farmers():
    return MOCK_FARMERS

@app.post("/api/v1/trigger-delta-alert")
def trigger_delta_alert(delta: PolicyDelta):
    affected_farmers = find_affected_farmers(delta, MOCK_FARMERS)
    alerts = [generate_voice_dispatch(farmer, delta) for farmer in affected_farmers]
    
    return {
        "success": True,
        "policy_update": delta.scheme_name,
        "total_affected_farmers": len(affected_farmers),
        "dispatched_alerts": alerts
    }

# Frontend serve karne ke liye static directory check
if os.path.exists("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")
  
