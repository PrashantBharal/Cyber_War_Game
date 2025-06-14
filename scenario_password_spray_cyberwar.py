# scenarios/scenario_password_spray_cyberwar.py

phases = [
    {
        "phase_title": "Phase 1 – Early Alert (0 min → 30 min)",
        "brief": (
            "Microsoft Entra ID (Azure AD) fires a “Password spray detected” alert: "
            "1 800 failed log-ins against 75 corporate accounts in five minutes."
        ),
        "questions": [
            {
                "dialogue": [
                    ("NOC Operator 08:02", "I’m seeing a spike of failed log-ins from random IPs."),
                    ("SOC Analyst", "As the NOC Operator, what’s your first action?")
                ],
                "question": "As the NOC Operator, what’s your first action?",
                "options": [
                    "A Ignore and keep watching",
                    "B Open a Priority-1 incident and page the on-call SOC",
                    "C Reboot a domain controller",
                    "D Post a GIF in Slack"
                ],
                "correct_index": 1,  # “B Open a Priority-1 incident and page the on-call SOC”
                "outcome_correct": "SOC Analyst: “P-1 opened—IR team mobilising.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("SOC Analyst 08:07", "Logins are all for Office 365 legacy POP/IMAP endpoints."),
                    ("IR Lead", "As the SOC Analyst, which severity do you log?")
                ],
                "question": "As the SOC Analyst, which severity do you log?",
                "options": [
                    "A Low",
                    "B Medium",
                    "C High",
                    "D Info only"
                ],
                "correct_index": 2,  # “C High”
                "outcome_correct": "IR Lead: “Marked HIGH—password-breach playbook engaged.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 2 – Containment & Assessment (30 min → 3 h)",
        "brief": "Three accounts are now confirmed compromised; Duo reports MFA disabled on those users.",
        "questions": [
            {
                "dialogue": [
                    ("Help-Desk 09:15", "Compromised users are still working and haven’t noticed."),
                    ("CISO", "As Help-Desk, what immediate action do you take?")
                ],
                "question": "As Help-Desk, what immediate action do you take?",
                "options": [
                    "A Ask users to call back later",
                    "B Disable the accounts and initiate an enforced password + MFA reset",
                    "C Let them finish their tasks",
                    "D Delete their mailboxes"
                ],
                "correct_index": 1,  # “B Disable the accounts and initiate an enforced password + MFA reset”
                "outcome_correct": "CISO: “Accounts blocked—attack contained.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Legal 09:30", "If customer PII was exposed, what is our regulator-report window?"),
                    ("CISO", "As Legal Counsel, decide.")
                ],
                "question": "As Legal Counsel, decide.",
                "options": [
                    "A 72 hours",
                    "B 48 hours",
                    "C 24 hours under CERT-In breach-notification rules",
                    "D No mandatory reporting"
                ],
                "correct_index": 2,  # “C 24 hours under CERT-In breach-notification rules”
                "outcome_correct": "CISO: “Twenty-four-hour timer started—draft notice underway.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 3 – Business Impact (3 h → 8 h)",
        "brief": (
            "Attackers used one breached account to download the full employee phone directory; "
            "staff complain of forced logouts after global password reset."
        ),
        "questions": [
            {
                "dialogue": [
                    ("IT Service-Desk 12:20", "Global reset kicked 1 400 users offline."),
                    ("Infra Head", "As IT Service-Desk, how do you guide employees back in?")
                ],
                "question": "As IT Service-Desk, how do you guide employees back in?",
                "options": [
                    "A Ask them to invent any new password",
                    "B Direct them to the self-service password-reset portal with MFA enforcement",
                    "C Tell them to wait till tomorrow",
                    "D Share a master password"
                ],
                "correct_index": 1,  # “B Direct them to the self-service password-reset portal with MFA enforcement”
                "outcome_correct": "Infra Head: “Portal traffic high but smooth—users regain access.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Reporter 13:10", "Rumour: XYZ-Corp accounts were hacked. Comment?"),
                    ("PR Lead", "As PR Lead, choose your statement.")
                ],
                "question": "As PR Lead, choose your statement.",
                "options": [
                    "A “No comment.”",
                    "B “We detected unauthorised login attempts, contained them, and forced a company-wide password reset. No customer financial data was impacted.”",
                    "C “Everything’s fine.”",
                    "D Publish a list of affected users"
                ],
                "correct_index": 1,  # “B “We detected unauthorised login attempts…”
                "outcome_correct": "Reporter: “Balanced story published.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 4 – Post-Incident Review (Next Day)",
        "brief": (
            "Attack is over; insurers and the board demand evidence and a plan to prevent password breaches."
        ),
        "questions": [
            {
                "dialogue": [
                    ("Legal D+1", "The insurer wants proof of compromise and containment."),
                    ("Forensic Lead", "As Legal Counsel, which artefact do we hand over?")
                ],
                "question": "As Legal Counsel, which artefact do we hand over?",
                "options": [
                    "A Sales brochure PDF",
                    "B Excel sheet of guesses",
                    "C Immutable Azure-AD sign-in logs and Conditional-Access reports, digitally signed",
                    "D A meme"
                ],
                "correct_index": 2,  # “C Immutable Azure-AD sign-in logs and Conditional-Access reports…”
                "outcome_correct": "Investigator: “Signed logs received—claim processing starts.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            },
            {
                "dialogue": [
                    ("Board Chair", "How do we stop password attacks for good?"),
                    ("CISO", "As the Board, pick the highest-impact first investment.")
                ],
                "question": "As the Board, pick the highest-impact first investment.",
                "options": [
                    "A Hire more receptionists",
                    "B Company-wide move to passwordless FIDO2 keys with mandatory MFA fallback",
                    "C Repaint the office",
                    "D Cut the security budget"
                ],
                "correct_index": 1,  # “B Company-wide move to passwordless FIDO2 keys…”
                "outcome_correct": "CISO: “Budget approved—passwordless rollout scheduled.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    }
]

# Core Documents you’ll reference during play
core_documents = [
    "Password-Incident Playbook – containment, reset scripts, legacy-auth kill steps.",
    "MFA & Conditional-Access Policy – enforcement rules, exception list.",
    "CERT-In Breach-Notification Checklist – required fields, 24-hour clock.",
    "Self-Service Password-Reset (SSPR) Guide – user instructions and comms templates.",
    "Evidence-Handling SOP – hashing Azure-AD sign-in logs, preserving Conditional-Access data.",
    "Road-Map Template – passwordless FIDO2 keys, continuous dark-web credential monitoring."
]

# Lifecycle you’ll highlight
action_flow = (
    "Alert → P-1 Ticket → Severity HIGH → Account Disable & MFA Reset → Customer/Media Comms → "
    "CERT-In Notice → Immutable Logs → Passwordless Road-Map."
)
