import math

def calculate_emi(principal: float, annual_rate: float, tenure_years: float):
    monthly_rate = annual_rate / (12 * 100)
    months = tenure_years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months
    total_interest = total_payment - principal

    return emi, total_interest, total_payment
