def simple_interest(principal: float, rate: float, time: float) -> float:
    return (principal * rate * time) / 100


def compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    return amount - principal
