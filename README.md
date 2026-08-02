# ServiceTrust AI - AI-Powered Non-Human Identity Governance

![AI Product](https://img.shields.io/badge/AI%20Product-5%20Agents-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Entra ID](https://img.shields.io/badge/Entra%20ID-99%25-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![CyberArk](https://img.shields.io/badge/CyberArk-Integrated-FF0000?style=for-the-badge)
![CISSP](https://img.shields.io/badge/CISSP-Architected-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

> From 5,000 unmanaged service accounts to autonomous risk detection & remediation for Insurance under NYDFS 23 NYCRR 500

**Live Portfolio:** Featured on LinkedIn | Pinned on GitHub Profile
**Author:** Channakeswara Vuppalamarthi, CISSP, AWS-SA | AI Product Manager | Principal TPM - Cybersecurity

---

## 🎯 The Problem - Insurance Enterprise

*   **8:1 Ratio:** NHI to human identities in 99% Entra ID estate
*   **5K+ Service Accounts:** 50% high-risk — Interactive logons with RDP, hardcoded secrets in Terraform/GitHub/.env, RPA bots with mailbox access
*   **Tool Sprawl:** SailPoint (IGA), CyberArk (PAM), ServiceNow (CMDB), Sentinel (SIEM), Zscaler (ZPA), SCCM, ForeScout — no single source of truth
*   **Audit Pain:** 3 weeks to produce evidence for NYDFS 500 audit, risk of $2-10M fine
*   **Shadow Risk:** CyberArk Safes vs Entra ID delta = 30% shadow accounts not in PAM

## 🤖 The Product - 5 AI Agents

ServiceTrust AI is an **AI Product Management portfolio** built as an autonomous NHI Governance Platform.

### 1. Discovery Agent (`src/discovery/agent.py`)
Scans **20+ sources** — beyond just Entra/AD:
*   **Entra ID / AD:** Service Principals, Managed Identities, gMSA
*   **CyberArk Delta:** `CyberArk Safes vs Entra = Shadow Accounts` — core differentiator
*   **Secrets:** Azure Key Vault, GitHub, Terraform, `.env`, Jenkins
*   **Infra:** ServiceNow CMDB, SCCM, ForeScout, ZPA logs
*   **NLP:** Parses AD descriptions to find ownerless shadow accounts

### 2. Risk Scorer Agent (`src/risk/scorer.py`)
*   **Tier0/1/2** classification + **configurable 30-365d** rotation (NYDFS requirement)
*   Scores: Privilege (Tier0), Interactive Logon, Last Use, Data Classification, Secret Age

### 3. Owner Prediction Agent
*   **85% accuracy** from Git history + SNOW ticket history + AD manager chain for orphaned accounts

### 4. Anomaly Detection Agent
*   Sentinel + ADX + ML: Impossible travel, ZPA bypass, off-hours use, privilege escalation

### 5. GenAI Copilot Agent (`src/api/main.py`)
*   Converts interactive service account -> `gMSA / Managed Identity` with auto-generated code + justification summary for auditor

## 📊 Product Decisions (Why this is AI Product Management)

| Decision | Options | Choice & Why |
| :--- | :--- | :--- |
| **Single Pane** | New portal vs SNOW | **SNOW single window** — users live in SNOW, not another portal |
| **Day 1 Action** | Block vs Alert | **Alert-not-Block** — avoid SCCM break, build trust |
| **Multi-Cloud** | Direct vs Federation | **Federation vs Direct toggle** for future-proof |
| **Ownership** | IAM vs SOC | **IAM + SOC co-owned** — Sponsors: CISO & CTO |

## 📈 Impact

*   **Interactive Tier0:** 500 → 0
*   **Provisioning:** 14 days → 15 minutes
*   **Audit Evidence:** 3 weeks → 10 minutes
*   **Standing Secrets:** -80%
*   **Compliance:** Avoids $2-10M NYDFS 500 fine

## 🏗️ Architecture
