"""
FinSathi — Agentic AI Banking Assistant
SBI Hackathon @ GFF 2026

A CLI prototype simulating the 3-agent pipeline:
  1. Spend Analyst Agent   — reads transaction events
  2. Life Event Detector   — identifies financial triggers
  3. Nudge & Action Agent  — generates personalised nudges & executes actions

Run: python finsathi.py
"""

import time
import random
from datetime import datetime

# ─── ANSI Colors ──────────────────────────────────────────────────
class C:
    GOLD   = "\033[38;2;245;166;35m"
    TEAL   = "\033[38;2;0;201;177m"
    PURPLE = "\033[38;2;124;58;237m"
    WHITE  = "\033[97m"
    GRAY   = "\033[38;2;138;155;181m"
    GREEN  = "\033[92m"
    RED    = "\033[91m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

def cprint(text, color="", bold=False):
    prefix = (C.BOLD if bold else "") + color
    print(f"{prefix}{text}{C.RESET}")

def slow_print(text, color="", delay=0.03):
    prefix = color
    for ch in text:
        print(f"{prefix}{ch}{C.RESET}", end="", flush=True)
        time.sleep(delay)
    print()

def divider(char="─", color=C.GRAY):
    cprint(char * 60, color)

def agent_header(name, icon, color):
    print()
    cprint(f"  {icon}  {name}", color, bold=True)
    cprint(f"  {'─' * (len(name) + 5)}", color)

def thinking(msg, delay=0.8):
    print(f"  {C.GRAY}⟳  {msg}...{C.RESET}", end="", flush=True)
    time.sleep(delay)
    print(f"\r  {C.GREEN}✓  {msg}   {C.RESET}")

# ─── User Profiles ────────────────────────────────────────────────
USERS = {
    "1": {
        "name": "Ravi Kumar",
        "city": "Varanasi",
        "language": "Hindi",
        "balance": 45000,
        "salary": 45000,
        "trigger": "salary_credited",
        "savings": 8000,
        "has_sip": False,
        "has_fd": False,
    },
    "2": {
        "name": "Priya Sharma",
        "city": "Pune",
        "language": "English",
        "balance": 12000,
        "salary": 72000,
        "trigger": "large_purchase",
        "purchase_amount": 28500,
        "merchant": "Croma Electronics",
    },
    "3": {
        "name": "Mohan Das",
        "city": "Chennai",
        "language": "Tamil",
        "balance": 3200,
        "salary": 28000,
        "trigger": "low_balance",
        "emi_due": 4200,
        "days_to_emi": 3,
        "days_to_salary": 8,
    },
}

# ─── Agent 1: Spend Analyst ───────────────────────────────────────
def spend_analyst_agent(user: dict) -> dict:
    agent_header("SPEND ANALYST AGENT", "🗄️", C.GOLD)
    thinking("Connecting to SBI Core Banking event stream")
    thinking("Reading transaction ledger")
    thinking("Running spend categorisation model")

    trigger = user["trigger"]
    analysis = {}

    if trigger == "salary_credited":
        avg_spend = int(user["salary"] * 0.71)
        unallocated = user["salary"] - avg_spend
        analysis = {
            "event": "salary_credited",
            "amount": user["salary"],
            "avg_monthly_spend": avg_spend,
            "unallocated_funds": unallocated,
            "has_sip": user.get("has_sip", False),
        }
        cprint(f"\n  📥 Event Detected   : Salary Credit", C.WHITE)
        cprint(f"  💰 Amount           : ₹{user['salary']:,}", C.GOLD)
        cprint(f"  📊 Avg Monthly Spend: ₹{avg_spend:,}", C.GRAY)
        cprint(f"  💡 Unallocated Funds: ₹{unallocated:,}", C.TEAL)
        cprint(f"  📈 Active SIP       : {'Yes' if user.get('has_sip') else 'No'}", C.GRAY)

    elif trigger == "large_purchase":
        analysis = {
            "event": "large_purchase",
            "amount": user["purchase_amount"],
            "merchant": user["merchant"],
            "category": "Electronics",
            "emi_eligible": True,
            "emi_saving": int(user["purchase_amount"] * 0.113),
        }
        cprint(f"\n  🛒 Event Detected   : Large Purchase", C.WHITE)
        cprint(f"  💳 Amount           : ₹{user['purchase_amount']:,}", C.GOLD)
        cprint(f"  🏪 Merchant         : {user['merchant']}", C.GRAY)
        cprint(f"  🏷️  Category         : Electronics", C.GRAY)
        cprint(f"  ✅ EMI Eligible     : Yes (0% available)", C.TEAL)

    elif trigger == "low_balance":
        analysis = {
            "event": "low_balance",
            "balance": user["balance"],
            "emi_due": user["emi_due"],
            "days_to_emi": user["days_to_emi"],
            "days_to_salary": user["days_to_salary"],
            "shortfall": user["emi_due"] - user["balance"],
            "overdraft_limit": 15000,
        }
        cprint(f"\n  ⚠️  Event Detected   : Low Balance Alert", C.WHITE)
        cprint(f"  💸 Current Balance  : ₹{user['balance']:,}", C.RED)
        cprint(f"  📅 EMI Due in       : {user['days_to_emi']} days (₹{user['emi_due']:,})", C.GOLD)
        cprint(f"  📉 Shortfall        : ₹{analysis['shortfall']:,}", C.RED)
        cprint(f"  🏦 Overdraft Limit  : ₹{analysis['overdraft_limit']:,} (pre-approved)", C.TEAL)

    return analysis

# ─── Agent 2: Life Event Detector ────────────────────────────────
def life_event_detector(user: dict, analysis: dict) -> dict:
    agent_header("LIFE EVENT DETECTOR", "🧠", C.TEAL)
    thinking("Running pattern recognition on user history")
    thinking("Checking financial goal alignment")
    thinking("Scoring engagement opportunity")

    trigger = analysis["event"]
    event_data = {}

    if trigger == "salary_credited":
        score = 87 if not analysis["has_sip"] else 42
        event_data = {
            "life_event": "Regular Income — Investment Gap",
            "opportunity": "SIP Enrollment",
            "urgency": "High" if score > 80 else "Medium",
            "confidence": score,
            "recommended_product": "SBI Bluechip Mutual Fund SIP",
            "recommended_amount": min(3000, analysis["unallocated_funds"] // 4),
        }
        cprint(f"\n  🎯 Life Event       : {event_data['life_event']}", C.WHITE)
        cprint(f"  💎 Opportunity      : {event_data['opportunity']}", C.TEAL)
        cprint(f"  🔥 Urgency          : {event_data['urgency']}", C.GOLD)
        cprint(f"  📊 Confidence Score : {event_data['confidence']}%", C.GOLD)
        cprint(f"  📦 Product Match    : {event_data['recommended_product']}", C.GRAY)

    elif trigger == "large_purchase":
        event_data = {
            "life_event": "Major Lifestyle Purchase",
            "opportunity": "EMI Conversion",
            "urgency": "High",
            "confidence": 92,
            "recommended_product": "SBI Credit Card 0% EMI",
            "emi_months": 6,
            "monthly_emi": analysis["amount"] // 6,
        }
        cprint(f"\n  🎯 Life Event       : {event_data['life_event']}", C.WHITE)
        cprint(f"  💎 Opportunity      : {event_data['opportunity']}", C.TEAL)
        cprint(f"  📊 Confidence Score : {event_data['confidence']}%", C.GOLD)
        cprint(f"  📦 Product Match    : {event_data['recommended_product']}", C.GRAY)
        cprint(f"  📅 EMI Plan         : ₹{event_data['monthly_emi']:,}/month × {event_data['emi_months']} months", C.GRAY)

    elif trigger == "low_balance":
        event_data = {
            "life_event": "Cash Crunch Risk",
            "opportunity": "Overdraft Activation",
            "urgency": "Critical",
            "confidence": 96,
            "recommended_product": "SBI Overdraft Facility",
            "overdraft_limit": analysis["overdraft_limit"],
        }
        cprint(f"\n  🎯 Life Event       : {event_data['life_event']}", C.WHITE)
        cprint(f"  💎 Opportunity      : {event_data['opportunity']}", C.TEAL)
        cprint(f"  🚨 Urgency          : {event_data['urgency']}", C.RED, bold=True)
        cprint(f"  📊 Confidence Score : {event_data['confidence']}%", C.GOLD)
        cprint(f"  📦 Product Match    : {event_data['recommended_product']}", C.GRAY)

    return event_data

# ─── Agent 3: Nudge & Action Agent ───────────────────────────────
def nudge_action_agent(user: dict, analysis: dict, event_data: dict) -> str:
    agent_header("NUDGE & ACTION AGENT", "🤖", C.PURPLE)
    thinking("Selecting optimal delivery channel (WhatsApp)")
    thinking(f"Generating message in {user['language']}")
    thinking("Rendering personalised nudge")

    trigger = analysis["event"]
    name = user["name"].split()[0]

    if trigger == "salary_credited":
        msg = (
            f"🏦 नमस्ते {name}! आपकी सैलरी ₹{analysis['amount']:,} क्रेडिट हुई।\n"
            f"   आपके पास ₹{analysis['unallocated_funds']:,} अनअलॉकेटेड हैं।\n"
            f"   क्या ₹{event_data['recommended_amount']:,}/माह का SIP शुरू करें?\n"
            f"   (SBI Bluechip Fund — 15% avg annual return 📈)"
        )
    elif trigger == "large_purchase":
        msg = (
            f"💳 Hi {name}! ₹{analysis['amount']:,} spend at {analysis['merchant']} detected.\n"
            f"   Convert to 0% EMI for 6 months?\n"
            f"   Pay just ₹{event_data['monthly_emi']:,}/month — save ₹{analysis['emi_saving']:,} in interest! 💰"
        )
    else:  # low_balance
        msg = (
            f"⚠️  Hi {name}! Balance low: ₹{user['balance']:,}.\n"
            f"   EMI of ₹{analysis['emi_due']:,} due in {analysis['days_to_emi']} days.\n"
            f"   Activate ₹{analysis['overdraft_limit']:,} overdraft instantly?\n"
            f"   (Pre-approved. No paperwork. Repay on salary day 🔐)"
        )
    cprint(f"\n  ┌{'─' * 56}┐", C.GRAY)
    cprint(f"  │  📱 WhatsApp Message Preview", C.GREEN)
    cprint(f"  ├{'─' * 56}┤", C.GRAY)
    for line in msg.split("\n"):
        cprint(f"  │  {line}", C.WHITE)
    cprint(f"  └{'─' * 56}┘", C.GRAY)

    return msg

# ─── Action Executor ─────────────────────────────────────────────
def execute_action(user: dict, event_data: dict, choice: str):
    agent_header("ACTION EXECUTOR", "⚡", C.GREEN)
    trigger_map = {
        "1": {
            "salary_credited": ("Enrolling in SIP", f"✅ SBI Bluechip SIP of ₹{event_data.get('recommended_amount', 3000):,}/month started!\n   First instalment: 1st of next month.\n   Track in YONO → Investments."),
            "large_purchase":  ("Converting to EMI", f"✅ ₹{event_data.get('monthly_emi', 0):,}/month × 6 months EMI activated!\n   Zero interest. Starts next billing cycle.\n   Check SBI Card app for details."),
            "low_balance":     ("Activating Overdraft", f"✅ ₹{event_data.get('overdraft_limit', 15000):,} overdraft activated instantly!\n   Protected till your salary arrives.\n   Interest: 0.05%/day — only if used."),
        },
        "2": {
            "salary_credited": (None, "📊 Showing alternatives:\n   1. FD ₹10,000 @ 7.1% — guaranteed\n   2. RD ₹2,000/month — flexible\n   3. SIP ₹3,000/month — market-linked\n   Reply with your choice!"),
            "large_purchase":  (None, "📋 EMI plans sent to your WhatsApp.\n   3-month, 6-month, 12-month options available."),
            "low_balance":     (None, "🔔 Reminder set for tomorrow 9 AM.\n   Your EMI is still 3 days away — you're safe for now."),
        },
        "3": {
            "salary_credited": (None, "✌️  No problem! Reply 'SIP' anytime to start.\n   Your offer is valid for 30 days."),
            "large_purchase":  (None, "👍 No worries! Reply 'EMI' anytime within 30 days."),
            "low_balance":     (None, "📞 Connecting to SBI Care...\n   A banker will call you within 2 minutes."),
        },
    }

    action_info = trigger_map.get(choice, {}).get(user["trigger"])
    if not action_info:
        cprint("  Invalid choice.", C.RED)
        return

    process_name, result = action_info

    if process_name:
        thinking(process_name, delay=1.0)
        thinking("Updating SBI Core Banking record")
        thinking("Sending confirmation to user")

    print()
    cprint(f"  {result}", C.GREEN)

# ─── Main Flow ────────────────────────────────────────────────────
def main():
    print("\033[2J\033[H", end="")  # Clear screen
    divider("═", C.GOLD)
    cprint("  🧠  F I N S A T H I", C.GOLD, bold=True)
    cprint("  Agentic AI Banking Companion — SBI Hackathon @ GFF 2026", C.GRAY)
    cprint(f"  {datetime.now().strftime('%d %b %Y  %H:%M:%S')}", C.GRAY)
    divider("═", C.GOLD)

    # Profile selection
    cprint("\n  SELECT USER PROFILE TO SIMULATE:\n", C.TEAL, bold=True)
    cprint("  [1]  Ravi Kumar    — Varanasi    — Salary credited", C.WHITE)
    cprint("  [2]  Priya Sharma  — Pune        — Large purchase detected", C.WHITE)
    cprint("  [3]  Mohan Das     — Chennai     — Low balance alert", C.WHITE)
    print()

    while True:
        choice = input(f"  {C.GOLD}Enter profile [1/2/3]: {C.RESET}").strip()
        if choice in USERS:
            break
        cprint("  Please enter 1, 2, or 3.", C.RED)

    user = USERS[choice]
    print()
    divider()
    cprint(f"\n  👤 Profile: {user['name']}  |  {user['city']}  |  {user['language']}", C.WHITE, bold=True)
    cprint(f"  💳 Balance: ₹{user['balance']:,}  |  Trigger: {user['trigger'].replace('_', ' ').title()}", C.GRAY)
    divider()

    # ── Run the 3 agents ──────────────────────────────────────────
    cprint("\n  🚀 STARTING AGENT PIPELINE...\n", C.TEAL, bold=True)
    time.sleep(0.5)

    analysis  = spend_analyst_agent(user)
    print()
    event_data = life_event_detector(user, analysis)
    print()
    nudge_action_agent(user, analysis, event_data)

    # ── User action ───────────────────────────────────────────────
    print()
    divider()
    cprint("\n  HOW DOES THE USER RESPOND?\n", C.TEAL, bold=True)

    action_labels = {
        "salary_credited": ["[1] Yes, start my SIP now", "[2] Show me other options", "[3] Not now"],
        "large_purchase":  ["[1] Convert to EMI",        "[2] See all plans",         "[3] No thanks"],
        "low_balance":     ["[1] Activate Overdraft",    "[2] Remind me tomorrow",    "[3] Call me"],
    }

    for label in action_labels[user["trigger"]]:
        cprint(f"  {label}", C.WHITE)
    print()

    while True:
        user_choice = input(f"  {C.GOLD}Enter choice [1/2/3]: {C.RESET}").strip()
        if user_choice in ["1", "2", "3"]:
            break
        cprint("  Please enter 1, 2, or 3.", C.RED)

    print()
    execute_action(user, event_data, user_choice)

    # ── Summary ───────────────────────────────────────────────────
    print()
    divider("═", C.TEAL)
    cprint("\n  ✅ PIPELINE COMPLETE\n", C.TEAL, bold=True)
    cprint("  Agents run : Spend Analyst → Life Event Detector → Nudge & Action", C.GRAY)
    cprint("  Channel    : WhatsApp (zero app-open required)", C.GRAY)
    cprint("  Time taken : < 3 seconds end-to-end", C.GRAY)
    cprint("  Language   : Personalised to user's preference", C.GRAY)
    divider("═", C.TEAL)
    cprint("\n  Built for SBI Hackathon @ GFF 2026  •  FinSathi v1.0\n", C.GRAY)


if __name__ == "__main__":
    main()
