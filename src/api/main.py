
from fastapi import FastAPI
from src.discovery.agent import AIDiscoveryAgent
from src.risk.scorer import score_risk

app = FastAPI(title="ServiceTrust AI - NHI Governance")

@app.get("/")
def root():
    return {"product": "ServiceTrust AI", "author": "Channakeswara Vuppalamarthi", "agents": 5}

@app.get("/discover")
def discover():
    agent = AIDiscoveryAgent()
    findings = agent.run_full_discovery()
    for f in findings:
        f.update(score_risk(f))
    return {"total": len(findings), "findings": findings}

@app.get("/copilot/remediate/{account_id}")
def copilot_remediate(account_id: str):
    code = f"""
    # AI Generated Remediation for {account_id} - Critical Interactive
    New-ADServiceAccount -Name gMSA-{account_id} -DNSHostName gMSA-{account_id}.contoso.com -PrincipalsAllowedToRetrieveManagedPassword "ClaimsServers"
    # Use Managed Identity in app: DefaultAzureCredential()
    """
    return {"account": account_id, "ai_code": code, "justification": "Interactive with Domain Admin allows lateral movement bypassing ZPA. Convert to gMSA."}
