import streamlit as st

def calculate_federal_tax(annual_salary):
    brackets = [
        (0, 11000, 0.10),
        (11000, 44725, 0.12),
        (44725, 95375, 0.22),
        (95375, 182100, 0.24),
        (182100, 231250, 0.32),
        (231250, 578125, 0.35),
        (578125, float('inf'), 0.37)
    ]
    tax = 0
    for lower, upper, rate in brackets:
        if annual_salary > lower:
            taxable_income = min(annual_salary, upper) - lower
            tax += taxable_income * rate
        else:
            break
    return tax

def calculate_pay_details(annual_salary):
    hours_per_year = 2080
    pay_periods_per_year = 26
    federal_tax = calculate_federal_tax(annual_salary)
    utah_tax = annual_salary * 0.0465
    ss_tax = min(annual_salary, 168600) * 0.062
    medicare_tax = annual_salary * 0.0145
    total_tax = federal_tax + utah_tax + ss_tax + medicare_tax
    hourly_wage = annual_salary / hours_per_year
    gross_biweekly = annual_salary / pay_periods_per_year
    net_biweekly = (annual_salary - total_tax) / pay_periods_per_year
    effective_tax_rate = total_tax / annual_salary * 100
    return hourly_wage, gross_biweekly, net_biweekly, effective_tax_rate

# Streamlit UI
st.set_page_config(page_title="Retirement Calculator", layout="centered")
st.title("💰 Retirement Income Calculator")

salary = st.number_input("Enter your annual salary ($):", min_value=0, step=1000, value=100000)

if st.button("Calculate"):
    hourly, gross, net, tax_rate = calculate_pay_details(salary)
    st.markdown("### Results")
    st.write(f"**Hourly Wage:** ${hourly:.2f}")
    st.write(f"**Biweekly Gross:** ${gross:.2f}")
    st.write(f"**Biweekly Net:** ${net:.2f}")
    st.write(f"**Effective Tax Rate:** {tax_rate:.2f}%")

