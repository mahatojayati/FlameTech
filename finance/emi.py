def calculate_emi(p: float, annual_rate: float, years: int) -> float:
    r = annual_rate / (12 * 100)
    n = years * 12
    numerator = p * r * (1 + r) ** n
    denominator = (1 + r) ** n - 1
    return numerator / denominator