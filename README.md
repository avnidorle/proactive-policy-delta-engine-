# proactive-policy-delta-engine-
AI-powered government policy change detection and personalized farmer assistance system
<img width="1911" height="907" alt="image" src="https://github.com/user-attachments/assets/6b000ace-de42-45d8-bd68-686f75fc5ece" />
# 🌾 Proactive Policy Delta Engine

> An AI-powered government policy change detection, AgriStack rule-filtering, and regional voice-guidance engine built for rural beneficiaries.

---

## 📸 System Dashboard Preview

<!-- Yahan cursor rakh kar seedha Ctrl + V press karein screenshot paste karne ke liye -->

---

## 📌 Problem Statement

Government agriculture portals and ministries routinely update policy guidelines, application deadlines, and compliance rules (such as e-KYC mandates) via unnotified circulars and PDF revisions. 

Because small and marginal farmers often face literacy barriers and lack real-time digital access:
- Critical deadline extensions and subsidy opportunities are missed.
- Generic blast SMS messages lead to alert fatigue and irrelevant spam.
- Actionable steps (e.g., specific documents required at local CSCs) are rarely communicated in simple, regional vernacular formats.

---

## 💡 The Solution

The **Proactive Policy Delta Engine** replaces static aggregators with an active push-intelligence pipeline:

1. **Automated Delta Detection:** Ingests official policy updates and isolates exact diffs/revisions using NLP & LLM parsing.
2. **Hyper-Targeted AgriStack Matching:** Queries policy criteria (state, crop type, landholding thresholds) against farmer profiles to trigger zero-spam, relevant alerts.
3. **Action-Oriented Voice Guidance:** Converts policy deltas into regional-language voice scripts with step-by-step instructions.
4. **Dead-End Resolution:** Embeds local Common Service Centre (CSC) toll-free support and touchpoints directly into dispatch payloads.

---

## 🏗️ System Architecture

```text
       [ Official Gov / Portal Circulars ]
                         │
                         ▼
             ┌───────────────────────┐
             │  Policy Delta Engine  │ (Gemini / Diff Extraction)
             └───────────┬───────────┘
                         │ Structured JSON Criteria
                         ▼
             ┌───────────────────────┐
             │  AgriStack Matchmaker │ (Rules Engine: Land, Crop, State)
             └───────────┬───────────┘
                         │ Filtered Beneficiaries
                         ▼
             ┌───────────────────────┐
             │ Multi-Modal Dispatch  │ (Regional Script + Dead-End Resolution)
             └───────────┬───────────┘
                         ▼
       [ WhatsApp Audio Notes / IVR Dispatches ]
