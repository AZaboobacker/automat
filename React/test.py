import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Set page config
st.set_page_config(page_title='Financial Budgeting App', page_icon=':dollar:', layout='wide')

# Custom CSS for styling
st.markdown("""
<style>
body {
    background-color: #f5f5f5;
}
.main-title {
    color: #2E4057;
    font-size: 4rem;
    font-weight: 700;
}
.sidebar .sidebar-content {
    background-color: #2E4057;
    color: white;
}
.big-font {
    font-size: 1.5rem;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# Function to add an expense
def add_expense(expense_list, expense_name, expense_amount, date, category):
    new_expense = {
        'Name': expense_name,
        'Amount': expense_amount,
        'Date': date,
        'Category': category
    }
    expense_list.append(new_expense)
    return expense_list

# Sidebar configuration
st.sidebar.title('Financial Budgeting App')
page = st.sidebar.selectbox('Navigate', ['Dashboard', 'Add Expense', 'Analytics'])

# Dummy data
if 'expense_list' not in st.session_state:
    st.session_state['expense_list'] = [
        {'Name': 'Rent', 'Amount': 1200, 'Date': '2023-01-05', 'Category': 'Housing'},
        {'Name': 'Groceries', 'Amount': 200, 'Date': '2023-01-10', 'Category': 'Food'},
        {'Name': 'Internet', 'Amount': 60, 'Date': '2023-01-20', 'Category': 'Utilities'}
    ]

# Dashboard page
if page == 'Dashboard':
    st.markdown('<h1 class="main-title">Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('### Financial Overview')
    expense_df = pd.DataFrame(st.session_state['expense_list'])
    st.dataframe(expense_df)

    st.markdown('### Summary')
    total_expense = expense_df['Amount'].sum()
    st.markdown(f'<p class="big-font">Total Expense: ${total_expense}</p>', unsafe_allow_html=True)

# Add Expense page
elif page == 'Add Expense':
    st.markdown('<h1 class="main-title">Add Expense</h1>', unsafe_allow_html=True)
    expense_name = st.text_input('Expense Name')
    expense_amount = st.number_input('Expense Amount', min_value=0.0, step=0.01)
    expense_date = st.date_input('Date', datetime.now())
    expense_category = st.selectbox('Category', ['Housing', 'Food', 'Utilities', 'Entertainment', 'Others'])

    if st.button('Add Expense'):
        st.session_state['expense_list'] = add_expense(st.session_state['expense_list'], expense_name, expense_amount, expense_date, expense_category)
        st.success('Expense Added!')

# Analytics page
elif page == 'Analytics':
    st.markdown('<h1 class="main-title">Analytics</h1>', unsafe_allow_html=True)
    st.markdown('### Expense Breakdown by Category')
    expense_df = pd.DataFrame(st.session_state['expense_list'])
    category_expense = expense_df.groupby('Category')['Amount'].sum().reset_index()
    st.bar_chart(category_expense.set_index('Category'))

    st.markdown('### Expense Trend Over Time')
    expense_df['Date'] = pd.to_datetime(expense_df['Date'])
    expense_trend = expense_df.groupby('Date')['Amount'].sum().reset_index()
    st.line_chart(expense_trend.set_index('Date'))