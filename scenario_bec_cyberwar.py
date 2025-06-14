# scenarios/scenario_bec_cyberwar.py

phases = [
    {
        "phase_title": "Phase 1 – Suspicious Login (0 min → 30 min)",
        "brief": "CFO’s O365 account logs in from Lagos ten minutes after a Pune login.",
        "questions": [
            {
                "dialogue": [
                    ("SOC Analyst", "We have impossible travel on CFO mailbox."),
                    ("IT Security Manager", "As the SOC Analyst, first move?")
                ],
                "question": "As the SOC Analyst, first move?",
                "options": [
                    "A Ignore",
                    "B Force MFA re-auth and suspend the session",
                    "C Send FYI email",
                    "D Disable CFO’s laptop"
                ],
                "correct_index": 1,  # “B Force MFA re-auth and suspend the session”
                "outcome_correct": "IT Sec: “Session killed, MFA challenge sent.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("IT Security Manager", "Mailbox audit shows new forwarding rule to gmail.com."),
                    ("CFO Delegate", "As IT Security Manager, what severity?")
                ],
                "question": "As IT Security Manager, what severity?",
                "options": [
                    "A Low",
                    "B Medium",
                    "C High",
                    "D Info"
                ],
                "correct_index": 2,  # “C High”
                "outcome_correct": "Delegate: “High severity logged—BEC playbook begun.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 2 – Fake Invoice (30 min → 3 h)",
        "brief": "Attackers email AP team a changed bank account for a ₹ 8 crore payment.",
        "questions": [
            {
                "dialogue": [
                    ("AP Clerk 11:00", "Bank details changed, looks urgent."),
                    ("Finance Manager", "As AP Clerk, verify how?")
                ],
                "question": "As AP Clerk, verify how?",
                "options": [
                    "A Reply to same email",
                    "B Call vendor on a known number from the master register",
                    "C Approve quickly",
                    "D Google the bank"
                ],
                "correct_index": 1,  # “B Call vendor on a known number from the master register”
                "outcome_correct": "Finance Manager: “Vendor confirms change is fake—payment blocked.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("PR Lead 11:30", "Rumour CFO got hacked."),
                    ("CEO", "As PR, what do we publish?")
                ],
                "question": "As PR, what do we publish?",
                "options": [
                    "A “No comment.”",
                    "B “We detected suspicious mail activity and prevented fraudulent transfer; investigation continues.”",
                    "C “Everything is normal.”",
                    "D Release email headers"
                ],
                "correct_index": 1,  # “B “We detected suspicious mail activity…”
                "outcome_correct": "Journalist: “Company acted fast—no funds lost.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 3 – Forensic Deep-Dive (3 h → 24 h)",
        "brief": "Audit shows the attacker used legacy POP/IMAP to bypass MFA.",
        "questions": [
            {
                "dialogue": [
                    ("Infra Head", "POP/IMAP still enabled for execs’ iPads."),
                    ("CISO", "As Infra Head, immediate control?")
                ],
                "question": "As Infra Head, immediate control?",
                "options": [
                    "A Leave it",
                    "B Disable legacy protocols organisation-wide and force modern auth",
                    "C Decommission O365",
                    "D Ask users later"
                ],
                "correct_index": 1,  # “B Disable legacy protocols organisation-wide…”
                "outcome_correct": "CISO: “Legacy auth killed—attack vector closed.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Legal Counsel", "Regulators need proof no PII left via mailbox."),
                    ("Forensic Lead", "As Legal, which artefact shows that?")
                ],
                "question": "As Legal, which artefact shows that?",
                "options": [
                    "A Screenshot of inbox",
                    "B eDiscovery export proving no PII attachments in compromised window",
                    "C Marketing PPT",
                    "D VPN logs"
                ],
                "correct_index": 1,  # “B eDiscovery export proving no PII attachments…”
                "outcome_correct": "Regulator: “eDiscovery accepted.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 4 – Board Debrief (D+2)",
        "brief": "No money lost, but board demands resilience.",
        "questions": [
            {
                "dialogue": [
                    ("Board Chair", "Top single fix?"),
                    ("CISO", "As Board, pick.")
                ],
                "question": "As Board, pick.",
                "options": [
                    "A Hire more lawyers",
                    "B Enforce MFA with conditional access and disable all basic auth globally",
                    "C Buy new CRM",
                    "D Bigger bonus pool"
                ],
                "correct_index": 1,  # “B Enforce MFA with conditional access…”
                "outcome_correct": "CISO: “Policy enforced—risk greatly reduced.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Risk Officer", "Metric to prove progress?"),
                    ("CISO", "As Risk Officer, choose.")
                ],
                "question": "As Risk Officer, choose.",
                "options": [
                    "A Coffee usage",
                    "B Percentage of mailboxes using legacy auth (target = 0 %)",
                    "C Colour of CFO laptop",
                    "D Number of social-media likes"
                ],
                "correct_index": 1,  # “B Percentage of mailboxes using legacy auth…”
                "outcome_correct": "Board: “Metric measurable—tracking monthly.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    }
]

# Business-E-Mail Compromise (BEC) – Core References
core_documents = [
    "Incident-Response Plan – session-kill script, severity HIGH trigger.",
    "O365 / Google Workspace Security Baseline – impossible-travel alerts, audit-log retention.",
    "Conditional-Access & MFA Policy – block legacy protocols, enforce strong auth.",
    "Fraud-Payment SOP – vendor call-back, dual approval, hold procedure.",
    "BCP Media & Customer FAQ – clear language for partners and press.",
    "eDiscovery / Mailbox Export Guide – pull evidence of exfiltration or PII leakage.",
    "Metrics Dashboard Template – legacy-auth percentage, phishing click-rate, MTTD/MTTR."
]

# Reinforcement Flow During Play
action_flow = (
    "Impossible-Travel Alert → Session Suspension & MFA Reset → Forward-Rule Kill & Mailbox Sweep → "
    "Fraud Attempt Blocked via Call-Back → Legacy-Auth Disabled → CERT-In / Board Brief → "
    "Immutable eDiscovery Package → Metrics: Legacy-Auth 0 % & MTTD/MTTR down."
)
