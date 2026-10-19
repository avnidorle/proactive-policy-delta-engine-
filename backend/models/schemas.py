from pydantic import BaseModel
from typing import List, Optional

class FarmerProfile(BaseModel):
    farmer_id: str
    name: str
    state: str
    district: str
    land_holding_hectares: float
    crops_grown: List[str]
    social_category: str          # General, OBC, SC, ST
    prior_schemes: List[str] = []
    preferred_language: str = "hi"
    phone_number: str

class PolicyDelta(BaseModel):
    scheme_name: str
    portal_source: str
    change_type: str             # "DEADLINE_EXTENSION", "ELIGIBILITY_CHANGE", "KYC_RULE"
    summary_diff: str            # Short 1-line exact delta
    target_criteria: dict        # e.g. {"state": "Maharashtra", "max_land": 2.0}
    actionable_instruction: str  # Direct instruction for farmer
    csc_contact: Optional[str] = "Nearest CSC: District Centre (Toll-Free: 1800-180-1551)"
