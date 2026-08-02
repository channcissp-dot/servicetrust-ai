
def score_risk(account):
    risk_score = 0
    tier = "Tier2"
    rotation_days = 365
    if account.get("interactive") and account.get("privileged"):
        risk_score = 100
        tier = "Tier0"
        rotation_days = 30
    elif "Hardcoded" in str(account.get("finding")):
        risk_score = 95
        tier = "Tier0"
        rotation_days = 30
    elif "Orphaned" in str(account.get("finding")):
        risk_score = 80
        tier = "Tier1"
        rotation_days = 90
    elif not account.get("vaulted"):
        risk_score = 70
        tier = "Tier1"
        rotation_days = 90
    return {"tier": tier, "score": risk_score, "rotation_days": rotation_days, "remediation": "Convert to Managed Identity/gMSA, Vault in CyberArk"}

if __name__ == "__main__":
    print(score_risk({"id": "svc_sqlprod", "interactive": True, "privileged": True}))
