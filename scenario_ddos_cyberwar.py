# scenarios/scenario_ddos_cyberwar.py

phases = [
    {
        "phase_title": "Phase 1 – Early Detection (0 min → 30 min)",
        "brief": "Traffic into the XYZ-Corp website jumps from 200 Mbps to 2 Gbps—mostly random UDP bursts.",
        "questions": [
            {
                "dialogue": [
                    ("NOC Engineer 08:02", "Inbound is 10× normal and climbing."),
                    ("SOC Analyst", "As the NOC Engineer, what do you do first?")
                ],
                "question": "As the NOC Engineer, what do you do first?",
                "options": [
                    "A Ignore it",
                    "B Raise a Priority-1 incident ticket and page the on-call SOC",
                    "C Shut the site down",
                    "D Just chat in Slack"
                ],
                "correct_index": 1,  # “B Raise a Priority-1 incident ticket and page the on-call SOC”
                "outcome_correct": "SOC Analyst: “P-1 logged—the response team is moving.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("SOC Analyst 08:05", "Flows show the same five source networks flooding us."),
                    ("IR Lead", "As the SOC Analyst, what severity do you record in the IRP?")
                ],
                "question": "As the SOC Analyst, what severity do you record in the IRP?",
                "options": [
                    "A Low",
                    "B Medium",
                    "C High",
                    "D Info only"
                ],
                "correct_index": 2,  # “C High”
                "outcome_correct": "IR Lead: “Severity HIGH—DDoS playbook engaged.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            }
        ]
    },
    {
        "phase_title": "Phase 2 – Attack Escalation (30 min → 2 h)",
        "brief": "Latency hits eight seconds; customers complain on Twitter; traffic spikes to 12 Gbps after the attacker switches to DNS amplification.",
        "questions": [
            {
                "dialogue": [
                    ("Customer-Support 08:40", "Call volume exploding—site is crawling."),
                    ("Infra Head", "As Customer-Support, what do you tell callers?")
                ],
                "question": "As Customer-Support, what do you tell callers?",
                "options": [
                    "A “Nothing is wrong.”",
                    "B Read packet-capture stats",
                    "C Acknowledge slowness and say a fix is in progress",
                    "D Forward callers to marketing"
                ],
                "correct_index": 2,  # “C Acknowledge slowness and say a fix is in progress”
                "outcome_correct": "Infra Head: “Consistent message—customers stay calm.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            },
            {
                "dialogue": [
                    ("ISP Liaison 09:10", "Our upstream provider says we’re saturating their port."),
                    ("Infra Head", "As the ISP Liaison, what do you ask for first?")
                ],
                "question": "As the ISP Liaison, what do you ask for first?",
                "options": [
                    "A Tell them to drop our whole connection",
                    "B Request an upstream null-route / black-hole for attack traffic",
                    "C Say it isn’t our problem",
                    "D Ignore the e-mail"
                ],
                "correct_index": 1,  # “B Request an upstream null-route / black-hole for attack traffic”
                "outcome_correct": "Infra Head: “ISP black-holes bad traffic; link usage drops.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 3 – Business Continuity & Mitigation (2 h → 4 h)",
        "brief": (
            "Internal defences are maxed. You can spin up the contracted cloud-scrubbing service "
            "(₹ 5 lakh per day), but enabling it may break partner APIs. At the same time VPN latency "
            "spikes because the same circuit carries internet and VPN."
        ),
        "questions": [
            {
                "dialogue": [
                    ("CFO 10:15", "The scrubbing centre costs a fortune."),
                    ("CISO", "As the CFO, what’s the call?")
                ],
                "question": "As the CFO, what’s the call?",
                "options": [
                    "A Refuse and hope the traffic wanes",
                    "B Approve immediate activation of the scrubbing provider",
                    "C Wait for next week’s board meeting",
                    "D Lay off one network admin instead"
                ],
                "correct_index": 1,  # “B Approve immediate activation of the scrubbing provider”
                "outcome_correct": "CISO: “Scrubber engaged—good traffic now 95 % clean.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            },
            {
                "dialogue": [
                    ("IT Help-Desk 11:40", "Field staff can’t reach VPN; same pipe is flooded."),
                    ("Infra Head", "As IT Help-Desk, what workaround do you offer first?")
                ],
                "question": "As IT Help-Desk, what workaround do you offer first?",
                "options": [
                    "A Tell staff to stop work",
                    "B Move them to the backup SSL-VPN endpoint in the other data-centre",
                    "C Share your admin password",
                    "D Suggest personal Gmail"
                ],
                "correct_index": 1,  # “B Move them to the backup SSL-VPN endpoint in the other data-centre”
                "outcome_correct": "Field Engineer: “Backup VPN works—tasks resume.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    },
    {
        "phase_title": "Phase 4 – Post-Attack Review (D + 1)",
        "brief": (
            "After 12 hours the flood dies down. Regulators, insurers and the board all want proof "
            "you handled it—and a plan to prevent recurrence."
        ),
        "questions": [
            {
                "dialogue": [
                    ("Legal Next-Day", "Law enforcement wants logs."),
                    ("Forensic Lead", "As Legal Counsel, which artefact do we hand over?")
                ],
                "question": "As Legal Counsel, which artefact do we hand over?",
                "options": [
                    "A Marketing brochure",
                    "B NetFlow CSV without hashes",
                    "C Scrubber and firewall logs exported with digital signatures",
                    "D A Tweet about the attack"
                ],
                "correct_index": 2,  # “C Scrubber and firewall logs exported with digital signatures”
                "outcome_correct": "Investigator: “Signed logs received—analysis begins.”",
                "outcome_wrong": "Incorrect. The correct answer is C."
            },
            {
                "dialogue": [
                    ("Board Chair", "How do we stop this next time?"),
                    ("CISO", "As the Board, where do we spend first for lasting protection?")
                ],
                "question": "As the Board, where do we spend first for lasting protection?",
                "options": [
                    "A Bigger staff party",
                    "B Sign a standing DDoS-scrubbing retainer and finish automated fail-over run-books",
                    "C New logo design",
                    "D Freeze all budgets"
                ],
                "correct_index": 1,  # “B Sign a standing DDoS-scrubbing retainer and finish automated fail-over run-books”
                "outcome_correct": "CISO: “Retainer funded—run-books drafted.”",
                "outcome_wrong": "Incorrect. The correct answer is B."
            }
        ]
    }
]

# Core Documents & Action Flow (for reference in play):
core_documents = [
    "DDoS Playbook – escalation list, ISP contacts, scrubbing procedures.",
    "BCP Comms Annex – customer and media scripts.",
    "Change-Control Matrix – emergency rules for load-balancer and ACL tweaks.",
    "DR & Fail-over Run-Books – how to swing VPN and APIs to alt sites.",
    "Evidence Checklist – securing flow logs, scrubber reports, packet captures.",
    "Metrics Dashboard – Time-to-Mitigate, peak legitimate throughput, customer call rate.",
    "Contract Binder – pricing and escalation clauses for ISPs and scrubbing vendors."
]

action_flow = (
    "Detection → Incident Ticket → Severity HIGH → Customer Comms → Rate-Limiting & ISP Black-Hole → "
    "Cloud Scrubbing → VPN Fail-over → Recovery Metrics → RCA with Signed Logs → Standing Retainer & Automated Run-Books."
)
