# scenarios/scenario_ransomware_cyberwar.py

phases = [
    {
        "phase_title": "Phase 1 – Strange Behaviour (0 min → 30 min)",
        "brief": "AV alerts show Office documents spawning unknown executables on two laptops.",
        "questions": [
            {
                "dialogue": [
                    ("Desktop Support 09:05", "Workstations 17 and 22 just opened files that dropped .exe payloads."),
                    ("SOC Analyst", "As Desktop Support, what’s your first containment step?")
                ],
                "question": "As Desktop Support, what’s your first containment step?",
                "options": [
                    "A Reboot both PCs",
                    "B Pull their network cables and disable Wi-Fi immediately",
                    "C Wait for nightly scan",
                    "D Email users to be careful"
                ],
                "correct_index": 1,  # “B Pull their network cables and disable Wi-Fi immediately”
                "outcome_correct": "SOC: “Isolated—no beaconing.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("SOC Analyst 09:10", "Suspicious EXEs are packing AES libraries."),
                    ("IR Lead", "As the SOC Analyst, how do you classify severity?")
                ],
                "question": "As the SOC Analyst, how do you classify severity?",
                "options": [
                    "A Low",
                    "B Medium",
                    "C High",
                    "D Info only"
                ],
                "correct_index": 2,  # “C High”
                "outcome_correct": "IR Lead: “Severity HIGH; ransomware playbook engaged.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 2 – Encryption Begins (30 min → 2 h)",
        "brief": "Network shares start filling with .locky files; file servers spike in I/O.",
        "questions": [
            {
                "dialogue": [
                    ("Infrastructure Lead 09:45", "File server IOPS off the chart."),
                    ("CISO", "As Infra Lead, what stops the bleed fastest?")
                ],
                "question": "As Infra Lead, what stops the bleed fastest?",
                "options": [
                    "A Shut down all servers",
                    "B Disable SMB on infected subnets and isolate the file server VLAN",
                    "C Pull the main power breaker",
                    "D Do nothing"
                ],
                "correct_index": 1,  # “B Disable SMB on infected subnets and isolate the file server VLAN”
                "outcome_correct": "CISO: “Encryption halted on shares.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("PR Lead 10:10", "Rumours of ransom notes on Twitter."),
                    ("CEO", "As PR Lead, what statement goes out now?")
                ],
                "question": "As PR Lead, what statement goes out now?",
                "options": [
                    "A “No comment.”",
                    "B “We are investigating a malware event; no customer data appears impacted.”",
                    "C “Everything is fine.”",
                    "D Release the ransom note"
                ],
                "correct_index": 1,  # “B “We are investigating a malware event…”
                "outcome_correct": "Journalist: “Balanced story—awaiting updates.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 3 – Extortion Demand (2 h → 6 h)",
        "brief": "Attackers demand 15 BTC for the decryption key; backups look intact.",
        "questions": [
            {
                "dialogue": [
                    ("CFO 12:15", "Pay or restore?"),
                    ("CISO", "As CFO, pick the path.")
                ],
                "question": "As CFO, pick the path.",
                "options": [
                    "A Pay immediately",
                    "B Refuse payment and start clean restore from last night’s backups",
                    "C Wait for bargain",
                    "D Ask attackers for a demo"
                ],
                "correct_index": 1,  # “B Refuse payment and start clean restore…”
                "outcome_correct": "CISO: “Restores started—no ransom paid.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Legal Counsel 12:30", "Regulators may ask about personal data."),
                    ("CPO", "As Legal, what first document must we freeze?")
                ],
                "question": "As Legal, what first document must we freeze?",
                "options": [
                    "A Screenshot of ransom note",
                    "B Data-classification register showing no PII stored on encrypted file shares",
                    "C Marketing plan",
                    "D Vendor brochure"
                ],
                "correct_index": 1,  # “B Data-classification register…”
                "outcome_correct": "CPO: “Evidence preserved—regulators informed.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 4 – Post-Incident Review (Next Day)",
        "brief": "Restores succeeded; outage = 6 hours. Insurer and board want lessons.",
        "questions": [
            {
                "dialogue": [
                    ("Insurer D+1", "Send us proof of root cause."),
                    ("Forensic Lead", "As Insurer Liaison, what artefact closes the claim fastest?")
                ],
                "question": "As Insurer Liaison, what artefact closes the claim fastest?",
                "options": [
                    "A Word doc summary only",
                    "B Signed timeline with hash-verified log sources and identified phishing origin",
                    "C Company newsletter",
                    "D Excel budget"
                ],
                "correct_index": 1,  # “B Signed timeline with hash-verified log sources…”
                "outcome_correct": "Insurer: “Claim approved.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("Board Chair", "Top spend to prevent this again?"),
                    ("CISO", "As Board, choose.")
                ],
                "question": "As Board, choose.",
                "options": [
                    "A Holiday party",
                    "B Enterprise-wide EDR with automatic isolation plus immutable backup storage",
                    "C New office plants",
                    "D Freeze hiring"
                ],
                "correct_index": 1,  # “B Enterprise-wide EDR with automatic isolation…”
                "outcome_correct": "CISO: “EDR and backups funded.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    }
]

# Ransomware Outbreak – Core References
core_documents = [
    "Ransomware Playbook – isolation steps, legal constraints on paying, negotiation template.",
    "Backup & Disaster-Recovery Policy – RPO/RTO, tested-restore evidence, offline copies.",
    "Endpoint Isolation Procedure – how to yank cables / disable VLANs in seconds.",
    "Incident-Response Plan (IRP) – severity matrix, on-call roster, CERT-In timer.",
    "Business-Continuity Comms Annex – customer, board and media draft statements.",
    "Evidence Checklist – hash-verified SIEM, EDR and volume-shadow copies.",
    "Cyber-Insurance Binder – notification clauses, claim forms, forensic panel contacts."
]

# Reinforced Flow During Play
action_flow = (
    "Detection → Immediate Network Isolation → HIGH Severity Log → Encryption Halt / Share Offline → "
    "Decide Restore vs Pay → Clean Restore from Backups → Post-mortem Timeline & Signed Logs → "
    "Board-Approved EDR + Immutable-Backup Roadmap."
)
