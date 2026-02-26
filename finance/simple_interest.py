from vedic_finance_engine.core.nikhilam import nikhilam_multiply

def calculate_simple_interest(p: float, r: float, t: float) -> float:
    product = nikhilam_multiply(int(p), int(r))
    total = nikhilam_multiply(product, int(t))
    return total / 100

