def calculate_compound_interest(p: float, r: float, t: int) -> float:
    amount = p * ((1 + r/100) ** t)
    return amount - p