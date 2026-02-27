import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_amortization_schedule(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / (12 * 100)
    months = int(tenure_years * 12)

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    balance = principal
    schedule = []

    for month in range(1, months + 1):
        interest = balance * monthly_rate
        principal_component = emi - interest
        balance -= principal_component

        schedule.append([
            month,
            emi,
            principal_component,
            interest,
            max(balance, 0)
        ])

    df = pd.DataFrame(schedule, columns=[
        "Month",
        "EMI",
        "Principal Paid",
        "Interest Paid",
        "Remaining Balance"
    ])

    return df


def plot_area_chart(df):
    plt.figure()
    plt.stackplot(
        df["Month"],
        df["Principal Paid"],
        df["Interest Paid"],
        labels=["Principal", "Interest"]
    )
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("EMI Cash Flow Over Time")
    plt.legend()
    return plt


def plot_pie_chart(total_principal, total_interest):
    plt.figure()
    plt.pie(
        [total_principal, total_interest],
        labels=["Principal", "Interest"],
        autopct="%1.1f%%"
    )
    plt.title("Principal vs Interest Distribution")
    return plt
