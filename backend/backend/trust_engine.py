def calculate_trust_score(sla, escalations, recovery_rate):
    return round((sla * 0.4 + recovery_rate * 0.5 - escalations * 0.1), 2)
