def calculate_productivity_score(
    total_utilization,
    client_utilization,
    request_minutes,
    training_minutes
):
    score = 0

    # Total Utilization (40 marks)
    score += min(total_utilization, 100) * 0.40

    # Client Utilization (30 marks)
    score += min(client_utilization, 100) * 0.30

    # Request Handling (20 marks)
    if request_minutes >= 300:
        score += 20
    elif request_minutes >= 180:
        score += 15
    elif request_minutes >= 60:
        score += 10

    # Training (10 marks)
    if training_minutes > 0:
        score += 10

    return round(score, 1)