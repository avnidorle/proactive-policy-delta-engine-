import os
import json
import google.generativeai as genai
from models.schemas import PolicyDelta

genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))

PROMPT_TEMPLATE = """
You are a Policy Delta Detection Engine. Compare the old scheme guidelines with the updated guidelines.
Extract ONLY the structural delta/changes in strict JSON format.

Old Guidelines:
{old_text}

New Guidelines:
{new_text}

JSON Output structure:
{{
  "scheme_name": "string",
  "portal_source": "string",
  "change_type": "DEADLINE_EXTENSION | ELIGIBILITY_CHANGE | KYC_RULE",
  "summary_diff": "Short 1-line exact delta",
  "target_criteria": {{"state": "Maharashtra", "max_land": 2.0}},
  "actionable_instruction": "Direct step-by-step guidance for the farmer"
}}
"""

def extract_policy_delta(old_text: str, new_text: str, source_portal: str) -> PolicyDelta:
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = PROMPT_TEMPLATE.format(old_text=old_text, new_text=new_text)
    
    response = model.generate_content(
        prompt, 
        generation_config={"response_mime_type": "application/json"}
    )
    data = json.loads(response.text)
    data["portal_source"] = source_portal
    return PolicyDelta(**data)
