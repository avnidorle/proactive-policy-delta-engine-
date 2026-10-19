from typing import List
from models.schemas import FarmerProfile, PolicyDelta

def find_affected_farmers(delta: PolicyDelta, farmers: List[FarmerProfile]) -> List[FarmerProfile]:
    affected = []
    criteria = delta.target_criteria

    for farmer in farmers:
        # State match
        if "state" in criteria and criteria["state"].lower() != farmer.state.lower():
            continue
            
        # Land size match (e.g. Small & Marginal farmers)
        if "max_land" in criteria and farmer.land_holding_hectares > criteria["max_land"]:
            continue
            
        # Crop match
        if "crops" in criteria:
            matching_crops = [c for c in farmer.crops_grown if c.lower() in [x.lower() for x in criteria["crops"]]]
            if not matching_crops:
                continue

        affected.append(farmer)
        
    return affected
