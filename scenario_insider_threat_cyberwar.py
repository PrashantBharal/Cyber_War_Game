# scenarios/scenario_insider_threat_cyberwar.py

phases = [
    {
        "phase_title": "Phase 1 – Suspicion Raised (0 min → 30 min)",
        "brief": (
            "The UEBA (User & Entity Behavior Analytics) platform flags that a database administrator, "
            "Raj, has just accessed 7 000 CRM records at 02:10 a.m.—well outside his usual 09:00–18:00 pattern."
        ),
        "questions": [
            {
                "dialogue": [
                    ("SOC Analyst 02:15", "Raj’s account pulled thousands of customer rows at 2 a.m."),
                    ("IR Lead", "As the SOC Analyst, what is your very first action?")
                ],
                "question": "As the SOC Analyst, what is your very first action?",
                "options": [
                    "A Do nothing and watch for another night",
                    "B Create a Priority-1 ticket, escalate to the on-call incident responder, and preserve the UEBA alert",
                    "C Reboot the CRM server",
                    "D Send Raj a friendly chat message"
                ],
                "correct_index": 1,  # “B Create a Priority-1 ticket…”
                "outcome_correct": "IR Lead: “P-1 opened—evidence preserved, response team activated.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("IR Lead 02:18", "The pull was to Raj’s desktop; no business ticket exists."),
                    ("CISO", "As the IR Lead, what severity do you log in the IR plan?")
                ],
                "question": "As the IR Lead, what severity do you log in the IR plan?",
                "options": [
                    "A Low",
                    "B Medium",
                    "C High (potential insider exfil)",
                    "D Info only"
                ],
                "correct_index": 2,  # “C High (potential insider exfil)”
                "outcome_correct": "CISO: “Severity HIGH—insider-threat playbook engaged.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 2 – Containment & Verification (30 min → 3 h)",
        "brief": (
            "Security tools now show Raj copying the same CRM .csv to a USB stick and disabling his OneDrive sync client. "
            "HR confirms he resigned yesterday, effective next month."
        ),
        "questions": [
            {
                "dialogue": [
                    ("Security Manager 03:00", "Raj’s USB port is active right now."),
                    ("Infra Head", "As the Security Manager, which immediate step do you take?")
                ],
                "question": "As the Security Manager, which immediate step do you take?",
                "options": [
                    "A Unplug the entire CRM server",
                    "B Remotely lock Raj’s workstation and disable all of his IAM tokens pending investigation",
                    "C Wait until business hours for a meeting",
                    "D Ask Raj to bring the USB stick to the SOC"
                ],
                "correct_index": 1,  # “B Remotely lock Raj’s workstation…”
                "outcome_correct": "Infra Head: “Account and workstation locked—no further copying possible.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Legal 03:20", "If customer PII is involved, regulators must be told fast."),
                    ("CISO", "As Legal Counsel, which disclosure clock applies?")
                ],
                "question": "As Legal Counsel, which disclosure clock applies?",
                "options": [
                    "A 72 hours (GDPR only)",
                    "B 48 hours",
                    "C 24 hours under CERT-In personal-data-breach rule",
                    "D No obligation until loss is proven"
                ],
                "correct_index": 2,  # “C 24 hours under CERT-In…””
                "outcome_correct": "CISO: “Twenty-four-hour notification draft started.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 3 – Business Impact (3 h → 8 h)",
        "brief": (
            "Forensic review shows Raj e-mailed the CSV to his personal Gmail before the lockout. "
            "Customer-support queues spike as rumours of a leak spread on social media."
        ),
        "questions": [
            {
                "dialogue": [
                    ("IT Help-Desk 06:30", "Raj is calling from home demanding access for ‘handover work’."),
                    ("HR", "As IT Help-Desk, what do you tell him?")
                ],
                "question": "As IT Help-Desk, what do you tell him?",
                "options": [
                    "A Re-enable his account temporarily",
                    "B Inform him his access is suspended under investigation and route all work through his manager",
                    "C Ignore the call",
                    "D Share a copy of the database via WeTransfer"
                ],
                "correct_index": 1,  # “B Inform him his access is suspended…”
                "outcome_correct": "HR: “Clear boundary set—no unsupervised access.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Reporter 07:10", "Sources claim an XYZ-Corp insider stole customer data. Comment?"),
                    ("PR Lead", "As PR Lead, choose your statement.")
                ],
                "question": "As PR Lead, choose your statement.",
                "options": [
                    "A “No comment.”",
                    "B “We detected unauthorised data activity, have contained the account, and are evaluating potential impact. There is no disruption to customer services.”",
                    "C “Everything is normal.”",
                    "D Publish Raj’s photo"
                ],
                "correct_index": 1,  # “B “We detected unauthorised data activity…””
                "outcome_correct": "Journalist: “Balanced story filed—awaiting updates.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 4 – Post-Incident Review (D + 1)",
        "brief": (
            "Evidence shows Raj exfiltrated one file; no other systems touched. Insurer, regulators and the board request evidence "
            "of actions and a prevention roadmap."
        ),
        "questions": [
            {
                "dialogue": [
                    ("Legal Next Day", "Regulator wants immutable evidence."),
                    ("Forensic Lead", "As Legal, what do we hand over?")
                ],
                "question": "As Legal, what do we hand over?",
                "options": [
                    "A Marketing slide deck",
                    "B Excel of user activity without hashes",
                    "C Digitally-signed EDR logs, e-mail header traces and USB audit records",
                    "D A meme about insiders"
                ],
                "correct_index": 2,  # “C Digitally-signed EDR logs, e-mail header traces and USB audit records”
                "outcome_correct": "Investigator: “Signed logs accepted—case file opened.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            },
            {
                "dialogue": [
                    ("Board Chair", "How do we ensure this never happens again?"),
                    ("CISO", "As the Board, pick the most effective first investment.")
                ],
                "question": "As the Board, pick the most effective first investment.",
                "options": [
                    "A More ping-pong tables",
                    "B Deploy company-wide Data-Loss‐Prevention (DLP) with USB blocking and behaviour analytics tied to HR off-boarding alerts",
                    "C Redesign the company logo",
                    "D Freeze security budget"
                ],
                "correct_index": 1,  # “B Deploy company-wide DLP with USB blocking and behaviour analytics…”
                "outcome_correct": "CISO: “Budget approved—DLP and HR off-boarding integration scheduled.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    }
]

# Core Documents to keep handy during play
core_documents = [
    "Insider-Threat Playbook – detection triggers, legal checklists, HR coordination.",
    "Off-boarding Checklist – immediate token disable, exit interview, asset return.",
    "CERT-In Breach-Notification Guide – 24-hour clock and required fields.",
    "USB & DLP Policy – technical controls for removable media and e-mail egress.",
    "Evidence-Handling SOP – hashing EDR logs, mailbox traces, USB-history artefacts.",
    "Road-Map Template – DLP rollout, privileged-access reviews, continuous UEBA tuning."
]

# Story arc to emphasise
action_flow = (
    "UEBA Alert → P-1 Ticket → Account & Device Lock → CERT-In Notification → "
    "Customer/Media Comms → Immutable Evidence → HR Off-boarding Review → Board-Funded DLP & UEBA Enhancements."
)
