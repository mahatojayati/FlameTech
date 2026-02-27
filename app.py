import streamlit as st
from vedic_engine.interest import simple_interest, compound_interest
from vedic_engine.emi import calculate_emi

from vedic_engine.charts import (
    generate_amortization_schedule,
    plot_area_chart,
    plot_pie_chart
)


st.set_page_config(
    page_title="Vedic Financial Compute Engine",
    layout="wide",
    page_icon="💰"
)

# Custom CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("<h1 class='main-title'>🏦 Vedic Financial Compute Engine</h1>", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Select Service",
    ["EMI Calculator", "Simple Interest", "Compound Interest"]
)

st.sidebar.markdown("---")
st.sidebar.info("Built using Nikhilam Sutra acceleration logic")

# EMI MODULE
if menu == "EMI Calculator":
    st.subheader("Loan EMI Calculator")

    col1, col2, col3 = st.columns(3)

    with col1:
        principal = st.number_input("Loan Amount (₹)", min_value=0.0)

    with col2:
        rate = st.number_input("Annual Interest Rate (%)", min_value=0.0)

    with col3:
        tenure = st.number_input("Tenure (Years)", min_value=0.0)

    if st.button("Calculate EMI"):
        emi, interest, total = calculate_emi(principal, rate, tenure)

        st.success(f"Monthly EMI: ₹ {emi:,.2f}")
        st.info(f"Total Interest: ₹ {interest:,.2f}")
        st.warning(f"Total Payment: ₹ {total:,.2f}")

# SIMPLE INTEREST
elif menu == "Simple Interest":
    st.subheader("Simple Interest Calculator")

    p = st.number_input("Principal (₹)", min_value=0.0)
    r = st.number_input("Rate (%)", min_value=0.0)
    t = st.number_input("Time (Years)", min_value=0.0)

    if st.button("Calculate Interest"):
        si = simple_interest(p, r, t)
        st.success(f"Simple Interest: ₹ {si:,.2f}")

# COMPOUND INTEREST
elif menu == "Compound Interest":
    st.subheader("Compound Interest Calculator")

    p = st.number_input("Principal (₹)", min_value=0.0)
    r = st.number_input("Rate (%)", min_value=0.0)
    t = st.number_input("Time (Years)", min_value=0.0)
    n = st.number_input("Compounding per Year", min_value=1)

    if st.button("Calculate Interest"):
        ci = compound_interest(p, r, t, n)
        st.success(f"Compound Interest: ₹ {ci:,.2f}")
