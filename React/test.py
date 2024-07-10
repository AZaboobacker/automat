import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Custom CSS for a sleek and modern look
st.markdown(
    """
    <style>
    body {
        background-color: #F5F5F5;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .main-title {
        font-size: 48px;
        color: #4e73df;
        text-align: center;
        margin-bottom: 16px;
    }
    .menu-title {
        font-size: 24px;
        font-weight: bold;
        color: #2e59d9;
        margin-bottom: 12px;
    }
    .card {
        background: white;
        border-radius: 10px;
        padding: 20px; 
        margin-bottom: 20px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    .button {
        background-color: #4e73df;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .button:hover {
        background-color: #2e59d9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create sidebar menu
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Dashboard", "Income", "Expenses", "Summary"])

# Title
st.markdown('<h1 class="main-title">Financial Budgeting App</h1>', unsafe_allow_html=True)

# Dashboard Page
if selection == "Dashboard":
    st.markdown('<h2 class="menu-title">Dashboard</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">Overview of your financial status:</div>', unsafe_allow_html=True)
    df = pd.DataFrame(np.random.randn(50, 3), columns=['Income', 'Expenses', 'Savings'])
    st.line_chart(df)

# Income Page
elif selection == "Income":
    st.markdown('<h2 class="menu-title">Income</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">Record your income sources:</div>', unsafe_allow_html=True)
    st.text_input("Source of Income:")
    st.number_input("Amount:")
    st.button("Add Income", key="income_button", css_class='button')

# Expenses Page
elif selection == "Expenses":
    st.markdown('<h2 class="menu-title">Expenses</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">Track your expenses:</div>', unsafe_allow_html=True)
    st.text_input("Type of Expense:")
    st.number_input("Amount:")
    st.button("Add Expense", key="expense_button", css_class='button')

# Summary Page
elif selection == "Summary":
    st.markdown('<h2 class="menu-title">Summary</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">Summary of your financial status:</div>', unsafe_allow_html=True)
    df_summary = pd.DataFrame({"Categories": ["Income", "Expenses", "Savings"], "Amount": [5000, 2000, 3000]})
    st.bar_chart(df_summary.set_index('Categories'))