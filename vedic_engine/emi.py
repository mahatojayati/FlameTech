import math

if st.button("Calculate EMI"):
    emi, interest, total = calculate_emi(principal, rate, tenure)

    st.success(f"Monthly EMI: ₹ {emi:,.2f}")
    st.info(f"Total Interest: ₹ {interest:,.2f}")
    st.warning(f"Total Payment: ₹ {total:,.2f}")

    # Generate Schedule
    df = generate_amortization_schedule(principal, rate, tenure)

    st.subheader("Amortization Schedule")
    st.dataframe(df)

    # Area Chart
    st.subheader("Long-Term EMI Cash Flow (Area Chart)")
    area_plot = plot_area_chart(df)
    st.pyplot(area_plot)

    # Pie Chart
    st.subheader("Principal vs Interest Breakdown")
    pie_plot = plot_pie_chart(principal, interest)
    st.pyplot(pie_plot)
