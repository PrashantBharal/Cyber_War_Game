# scenarios/scenario_phishing_cyberwar.py

phases = [
    {
        "phase_title": "Phase 1 – Early Discovery (0 min → 30 min)",
        "brief": (
            "A single employee at XYZ-Corp receives an invoice from xy-zcorp.com "
            "(look-alike domain). No other impact is visible—yet."
        ),
        "questions": [
            {
                "dialogue": [
                    ("User (09:07)", "“This invoice came from a sketchy domain—what do I click?”"),
                    ("Help-Desk (09:08)", "“We have a phishing SOP. As the User, decide.”")
                ],
                "question": "“As the User, what do you click first?”",
                "options": [
                    "A Delete the mail",
                    "B Forward it to a friend",
                    "C Hit the “Report Phish” button",
                    "D Reply asking if it’s real"
                ],
                "correct_index": 2,  # “C Hit the “Report Phish” button”
                "outcome_correct": "✅ Help-Desk: “Alert sent—evidence preserved.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is C."
            },
            {
                "dialogue": [
                    ("SOC (09:10)", "“Header shows a spoof; macro payload pings a C2.”"),
                    ("IR Lead", "“As the SOC analyst, what severity goes in the incident log?”")
                ],
                "question": "“What severity do you record?”",
                "options": [
                    "A Informational",
                    "B Low",
                    "C Medium",
                    "D High"
                ],
                "correct_index": 3,  # “D High”
                "outcome_correct": "✅ IR Lead: “Severity set to HIGH—regulatory timer starts.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is D."
            }
        ]
    },
    {
        "phase_title": "Phase 2 – Lateral Spread (30 min → 3 h)",
        "brief": (
            "Twelve mailboxes now have malicious forwarding rules; impossible-travel "
            "log-ins appear; social chatter starts."
        ),
        "questions": [
            {
                "dialogue": [
                    ("HR (10:20)", "“Locked-out staff are confused and calling nonstop.”"),
                    ("CISO", "“As HR, how do you communicate?”")
                ],
                "question": "“How do you communicate to affected users?”",
                "options": [
                    "A Blast everyone with jargon",
                    "B Wait for Security’s summary, then send a short FAQ to the affected users",
                    "C Say nothing",
                    "D Post “HR has no info” on the intranet"
                ],
                "correct_index": 1,  # “B Wait for Security’s summary, then send a short FAQ …”
                "outcome_correct": "✅ CISO: “Targeted FAQ drops panic immediately.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Legal (10:40)", "“CERT-In requires fast notification once impact is confirmed.”"),
                    ("CISO", "“As Legal Counsel, what’s our maximum window?”")
                ],
                "question": "“What is our maximum window to notify CERT-In?”",
                "options": [
                    "A 24 h",
                    "B 12 h",
                    "C 6 h",
                    "D 48 h"
                ],
                "correct_index": 2,  # “C 6 h”
                "outcome_correct": "✅ CISO: “Six-hour notice drafted—clock is running.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 3 – Business Impact (3 h → 8 h)",
        "brief": (
            "A compromised delegate account requests a ₹ 4.6 crore transfer and 300 MB of HR data "
            "is uploaded to a rogue OneDrive tenant; customers on Twitter ask if the company was hacked."
        ),
        "questions": [
            {
                "dialogue": [
                    ("Finance Bot (13:05)", "“Approval needed: ₹ 4.6 Cr to Vendor X.”"),
                    ("Finance Manager", "“As Finance Manager, how do I verify?”")
                ],
                "question": "“How do you verify this payment request?”",
                "options": [
                    "A Reply to the e-mail",
                    "B Phone the CFO on a known internal number",
                    "C Approve—it came from a delegate",
                    "D Wait until tomorrow"
                ],
                "correct_index": 1,  # “B Phone the CFO…”
                "outcome_correct": "✅ CFO: “Good catch—that request was fake.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Reporter (14:10)", "“We’re hearing XYZ-Corp e-mails were hacked.”"),
                    ("PR Lead", "“As PR Lead, what do we release first?”")
                ],
                "question": "“What statement do you release?”",
                "options": [
                    "A “No comment.”",
                    "B “We are actively containing a cyber incident; customer data remains secure.”",
                    "C “Everything’s fine.”",
                    "D Publish server IPs"
                ],
                "correct_index": 1,  # “B … customer data remains secure.”
                "outcome_correct": "✅ Journalist: “Story balanced—awaiting updates.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 4 – Post-Incident Review (Next Day)",
        "brief": (
            "Phishing wave is contained, passwords reset, and backups verified. Insurers, regulators, "
            "and the board all want evidence and a prevention roadmap."
        ),
        "questions": [
            {
                "dialogue": [
                    ("Legal (D+1)", "“CERT-In and the insurer both want official evidence.”"),
                    ("Forensic Lead", "“As Legal, which artefact do we hand over?”")
                ],
                "question": "“Which artefact do we hand over?”",
                "options": [
                    "A Marketing flyer",
                    "B NetFlow CSV without hashes",
                    "C Immutable SIEM and mailbox-audit logs with digital signatures",
                    "D A tweet about training"
                ],
                "correct_index": 2,  # “C Immutable SIEM …”
                "outcome_correct": "✅ Investigator: “Signed logs accepted—analysis begins.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is C."
            },
            {
                "dialogue": [
                    ("Board Chair", "“How do we stop this from happening again?”"),
                    ("CISO", "“As the Board, choose the most effective first investment.”")
                ],
                "question": "“Which investment do we approve first?”",
                "options": [
                    "A Bigger staff party",
                    "B Enterprise-wide MFA rollout plus automated inbox-rule alerts",
                    "C New logo rebrand",
                    "D Freeze budget"
                ],
                "correct_index": 1,  # “B Enterprise-wide MFA rollout …”
                "outcome_correct": "✅ CISO: “Funds approved—MFA rollout scheduled.”",
                "outcome_wrong": "❌ Incorrect. The correct answer is B."
            }
        ]
    }
]
