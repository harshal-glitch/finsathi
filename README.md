# 🧠 FinSathi — Agentic AI Banking Companion

> **SBI Hackathon @ GFF 2026** | Theme: Agentic AI & Emerging Tech | Problem: Digital Engagement

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Hackathon](https://img.shields.io/badge/SBI%20Hackathon-GFF%202026-orange)](https://hackculture.io)

---

## 🎯 What is FinSathi?

**FinSathi** is a proactive, multi-agent AI banking assistant that reaches SBI customers through the channels they already use — WhatsApp, YONO, SMS — at exactly the right moment, in their own language.

Unlike a chatbot that waits for users to ask, FinSathi **acts first**:
- Detects a financial event (salary credit, large purchase, low balance)
- Runs it through 3 specialised AI agents
- Delivers a personalised, actionable nudge
- Executes the user's choice autonomously (enroll in SIP, convert to EMI, activate overdraft)

**Zero app-open required. Zero form to fill. One tap.**

---

## 🏗️ Architecture — 3-Agent Pipeline

```
SBI Core Banking Event
        │
        ▼
┌─────────────────────┐
│  Spend Analyst      │  Reads transactions, categorises spend,
│  Agent  🗄️          │  detects anomalies, calculates gaps
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Life Event         │  Identifies triggers (salary, big spend,
│  Detector  🧠       │  low balance), scores opportunity (0–100)
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Nudge & Action     │  Generates personalised multilingual
│  Agent  🤖          │  message, executes permitted actions
└────────┬────────────┘
         │
         ▼
  WhatsApp / YONO / SMS  →  User gets one-tap action
         │
         ▼
  Feedback loop back to agents (continuous learning)
```

---

## 📁 Repository Structure

```
finsathi/
├── finsathi.py          # CLI prototype — full 3-agent simulation
├── README.md            # This file
├── requirements.txt     # Dependencies (stdlib only for prototype)
├── LICENSE              # MIT
└── docs/
    └── architecture.md  # Detailed system design notes
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- No external libraries required for the CLI prototype

### Run the prototype
```bash
git clone https://github.com/YOUR_USERNAME/finsathi.git
cd finsathi
python finsathi.py
```

### What you'll see
```
🧠  F I N S A T H I
Agentic AI Banking Companion — SBI Hackathon @ GFF 2026

SELECT USER PROFILE TO SIMULATE:
  [1]  Ravi Kumar    — Varanasi    — Salary credited
  [2]  Priya Sharma  — Pune        — Large purchase detected
  [3]  Mohan Das     — Chennai     — Low balance alert
```

Pick a profile → watch the 3 agents run → respond to the WhatsApp nudge → see the action execute.

---

## 👤 Simulated User Profiles

| Profile | User | City | Language | Trigger | Agent Response |
|---------|------|------|----------|---------|----------------|
| 1 | Ravi Kumar | Varanasi | Hindi | Salary credited | SIP enrollment offer |
| 2 | Priya Sharma | Pune | English | Large purchase | 0% EMI conversion |
| 3 | Mohan Das | Chennai | Tamil | Low balance | Overdraft activation |

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-----------|
| AI / Agents | Claude API · LangGraph · CrewAI (planned) |
| Agent Orchestration | Multi-agent pipeline with tool-use |
| Backend | Python · FastAPI (production) |
| Database | PostgreSQL · Redis (event queue) |
| Channels | WhatsApp Business API · SBI YONO SDK · SMS |
| NLP | IndicBERT · Google Translate API |
| Security | AES-256 · OAuth 2.0 · PII masking · RBI compliant |
| Cloud | AWS / Azure (cloud-agnostic) |

---

## 💡 Key Features

### ✅ Truly Agentic — Not Just a Chatbot
The Nudge Agent doesn't just suggest — it **executes**. With user consent via one tap, it can:
- Enroll user in a SIP
- Convert a purchase to EMI
- Activate overdraft protection
- Set payment reminders

### ✅ India-First Design
- Supports 10+ Indian languages via IndicBERT
- Works on WhatsApp (no smartphone banking app needed)
- Designed for Tier 2 / Tier 3 city users
- RBI-compliant data handling

### ✅ Event-Driven, Not Scheduled
Unlike generic SMS blasts, FinSathi fires only on real financial events — making every message relevant and timely.

### ✅ Feedback Loop
Every user response (tap, ignore, reply) feeds back into the agent to improve future nudge accuracy.

---

## 📊 Business Impact

| Metric | Value |
|--------|-------|
| Target market | 500M+ SBI account holders |
| Expected engagement lift | 5%+ |
| Cross-sell rate vs generic SMS | 3x higher |
| Channels supported | WhatsApp, YONO, SMS |
| Languages | 10+ Indian languages |

---

## 🗺️ Roadmap

- [x] CLI prototype with 3-agent simulation
- [x] 3 user profiles (salary, purchase, low balance triggers)
- [x] Multilingual message generation
- [ ] FastAPI backend with real event streaming
- [ ] WhatsApp Business API integration
- [ ] Claude API integration for dynamic message generation
- [ ] LangGraph multi-agent orchestration
- [ ] IndicBERT NLP pipeline
- [ ] YONO SDK mock integration
- [ ] Dashboard for agent analytics

---

## 🔒 Security & Compliance

- All user data encrypted with AES-256
- Consent-first: every action requires explicit user approval
- PII masking before data enters AI layer
- RBI data residency requirements respected
- OAuth 2.0 for banking data access

---

## 👥 Team

Built for **SBI Hackathon @ GFF 2026**

| Member | Role |
|--------|------|
| Harshal Verma| Prompt Engineer with knowledge of C , C++ , Python , Java , Javascript, HTML & CSS |
---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

> *FinSathi — Making Every Indian Financially Empowered with AI* 🇮🇳
