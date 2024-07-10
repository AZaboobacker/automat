import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from streamlit_option_menu import option_menu

# CSS Styling
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    color: #333;
}
.sidebar .sidebar-content {
    background-color: #ffffff;
}
.reportview-container .markdown-text-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.header {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    color: #004080;
}
.budget-table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.budget-table th, .budget-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
}
.budget-table th {
    background-color: #004080;
    color: white;
    padding-top: 12px;
    padding-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Budget", "Analytics", "Settings"],
        icons=["house", "cash-stack", "bar-chart", "gear"],
        menu_icon="cast",
        default_index=0,
    )

# Pages
if selected == "Home":
    st.markdown("<div class='header'>Financial Budgeting App</div>", unsafe_allow_html=True)
    st.write("Welcome to your financial budgeting app. Navigate through the menu to manage your budget!")

elif selected == "Budget":
    st.markdown("<div class='header'>Manage Your Budget</div>", unsafe_allow_html=True)
    budget_data = st.experimental_get_query_params()
    if 'expenses' not in budget_data:
        expenses = [
            {"Date": "2023-01-01", "Category": "Groceries", "Amount": 100},
            {"Date": "2023-01-05", "Category": "Utilities", "Amount": 50},
            {"Date": "2023-01-10", "Category": "Transport", "Amount": 30}
        ]
        budget_data['expenses'] = expenses
    else:
        expenses = budget_data['expenses']
    df = pd.DataFrame(expenses)
    st.table(df.style.set_table_styles([
        dict(selector="", props=[("border", "2px solid white")]),
    ]).set_properties(**{
        'border-color': 'blue',
        'font-size': '12pt',
        'background-color': 'white'})
 if st.button('Add Expense'):
     new_expense_date = st.date_input('Date', datetime.now())
     new_expense_category = st.selectbox('Category', ('Groceries', 'Utilities', 'Transport', 'Entertainment', 'Others'))
     new_expense_amount = st.number_input('Amount', min_value=0.0, format='%f')
     new_expense = {"Date": str(new_expense_date), "Category": new_expense_category, "Amount": new_expense_amount}
     expenses.append(new_expense)
     st.experimental_set_query_params(expenses=expenses)
 elif selected == "Analytics":
    st.markdown("<div class='header'>Budget Analytics</div>", unsafe_allow_html=True)
    df = pd.DataFrame(expenses)
    st.write("**Expense Summary**")
    fig, ax = plt.subplots()
    sns.barplot(x="Category", y="Amount", data=df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif selected == "Settings":
    st.markdown("<div class='header'>Settings</div>", unsafe_allow_html=True)
    st.write("This is the settings page. Customize your preferences here.")
