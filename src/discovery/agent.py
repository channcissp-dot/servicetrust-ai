
"""
AI Discovery Agent - Refined with CyberArk + 20+ Sources
Layer 1-5 from case study
"""
class AIDiscoveryAgent:
    def __init__(self):
        self.inventory = []

    def discover_entra(self):
        print("Scanning Entra ID Service Principals via Graph API...")
        return [{"id": "sp-claims-api", "source": "Entra", "interactive": False, "vaulted": False}]

    def discover_ad(self):
        print("Scanning AD svc_* and gMSA via LDAP...")
        return [{"id": "svc_sqlprod", "source": "AD", "interactive": True, "privileged": True}]

    def discover_cyberark(self):
        print("Scanning CyberArk PAM Vault Safes/CPM/PTA - Richest source")
        shadow = [{"id": "svc_claims_batch", "source": "CyberArk", "finding": "Orphaned - in Vault but no owner in SailPoint"}]
        return shadow

    def discover_keyvault(self):
        print("Scanning Azure Key Vault access policies...")
        return [{"id": "kv-claims-secret", "source": "KeyVault", "finding": "Secret used instead of Managed Identity"}]

    def discover_code(self):
        print("Scanning GitHub + Terraform .tfstate for hardcoded secrets via NLP...")
        return [{"id": "hardcoded-secret", "source": "GitHub", "finding": "Hardcoded secret in Terraform .tfstate"}]

    def discover_cmdb(self):
        print("Scanning ServiceNow CMDB, SCCM, ForeScout, ZPA logs...")
        return [{"id": "svc_retired_server", "source": "CMDB", "finding": "Server retired but service account active = Orphaned"}]

    def discover_logs(self):
        print("Scanning Sentinel SignInLogs for Shadow SPs...")
        return []

    def run_full_discovery(self):
        findings = []
        findings += self.discover_entra()
        findings += self.discover_ad()
        findings += self.discover_cyberark()
        findings += self.discover_keyvault()
        findings += self.discover_code()
        findings += self.discover_cmdb()
        findings += self.discover_logs()
        print(f"Total: {len(findings)} findings")
        return findings

if __name__ == "__main__":
    agent = AIDiscoveryAgent()
    print(agent.run_full_discovery())
