from models.schemas import FarmerProfile, PolicyDelta

def generate_voice_dispatch(farmer: FarmerProfile, delta: PolicyDelta) -> dict:
    regional_script = (
        f"Namaste {farmer.name}. {delta.scheme_name} me naya badlaav aaya hai: {delta.summary_diff}. "
        f"Aapko ye karna hoga: {delta.actionable_instruction}. "
        f"Madad ke liye: {delta.csc_contact}."
    )
    
    return {
        "farmer_id": farmer.farmer_id,
        "name": farmer.name,
        "phone": farmer.phone_number,
        "language": farmer.preferred_language,
        "audio_script": regional_script,
        "delivery_channel": "WhatsApp Audio Note / IVR Call",
        "nearest_csc_support": delta.csc_contact
    }
