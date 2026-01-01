def predict_recovery(amount, days_overdue):
    if days_overdue < 30:
        return "High"
    elif days_overdue < 90:
        return "Medium"
    return "Low"
