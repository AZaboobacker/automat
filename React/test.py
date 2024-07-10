import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Custom CSS for sleek look
st.markdown(
    "<style>\n"
    "body {background-color: #f4f4f9; font-family: 'Helvetica Neue', sans-serif;}\n"
    ".sidebar .sidebar-content {background: #333; color: #fff;}\n"
    "</style>",
    unsafe_allow_html=True
)

# Set up app
st.set_page_config(page_title='Financial Budgeting App', page_icon=':moneybag:')

# Setup navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Income", "Expenses", "Summary"])

# Initialize session state variables if not already set
if 'income_data' not in st.session_state:
    st.session_state['income_data'] = []
    st.session_state['expense_data'] = []

# Functions to add entries

def add_income(date, source, amount):
    st.session_state['income_data'].append({"date": date, "source": source, "amount": amount})

def add_expense(date, category, amount):
    st.session_state['expense_data'].append({"date": date, "category": category, "amount": amount})

# Pages
if selection == "Income":
    st.title('Income')
    date = st.date_input('Date')
    source = st.text_input('Source')
    amount = st.number_input('Amount', min_value=0.0, format='%f')
    if st.button('Add Income'):
        add_income(date, source, amount)
        st.success('Income added successfully!')
    st.write(pd.DataFrame(st.session_state['income_data']))

elif selection == "Expenses":
    st.title('Expenses')
    date = st.date_input('Date')
    category = st.text_input('Category')
    amount = st.number_input('Amount', min_value=0.0, format='%f')
    if st.button('Add Expense'):
        add_expense(date, category, amount)
        st.success('Expense added successfully!')
    st.write(pd.DataFrame(st.session_state['expense_data']))

elif selection == "Summary":
    st.title('Summary')
    df_income = pd.DataFrame(st.session_state['income_data'])
    df_expenses = pd.DataFrame(st.session_state['expense_data'])
    total_income = df_income['amount'].sum() if not df_income.empty else 0
    total_expenses = df_expenses['amount'].sum() if not df_expenses.empty else 0
    remaining_budget = total_income - total_expenses

    st.markdown(f'**Total Income:** ${total_income:.2f}')
    st.markdown(f'**Total Expenses:** ${total_expenses:.2f}')
    st.markdown(f'**Remaining Budget:** ${remaining_budget:.2f}')

    # Line Plot
    df_income['date'] = pd.to_datetime(df_income['date'])
    df_expenses['date'] = pd.to_datetime(df_expenses['date'])
    plt.figure(figsize=(10, 5))
    plt.plot(df_income['date'], df_income['amount'], label='Income', color='green')
    plt.plot(df_expenses['date'], df_expenses['amount'], label='Expenses', color='red')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Financial Summary')
    plt.legend()
    st.pyplot(plt)