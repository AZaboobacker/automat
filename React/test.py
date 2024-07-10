import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Custom CSS for a sleek look
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    .sidebar .sidebar-content {
        background-color: #4b5d67;
    }
    .sidebar .sidebar-content .element-container .stTextInput input {
        border: none;
        padding: 10px;
        font-size: 1em;
        color: white;
        background-color: #3b4a57;
    }
    .sidebar .sidebar-content .element-container button {
        background-color: #3b4a57;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
    .sidebar .sidebar-content .element-container button:hover {
        background-color: #566a7f;
    }
    .main .block-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4b5d67;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #3b4a57;
    }
    .stTextInput>div>div>input:focus {
        border-color: #ff4b4b;
        box-shadow: 0 0 0 0.2rem rgba(255,75,75,0.25);
        background-color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main streamlit app setup
st.title('Financial Budgeting App')
st.image('https://image-url-placeholder.com', use_column_width=True)

# Define sidebar menu
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Dashboard", "Transactions", "Analytics", "Settings"],
        icons=["house", "card-checklist", "bar-chart", "gear"],
        menu_icon="cast",
        default_index=0,
    )

    st.sidebar.title("Budgeting Calculator")
    income = st.sidebar.number_input("Monthly Income:", min_value=0)
    expenses = st.sidebar.number_input("Total Monthly Expenses:", min_value=0)

if selected == "Dashboard":
    st.header("Dashboard")
    st.write("Overview of financial status")

if selected == "Transactions":
    st.header("Transactions")
    st.write("Record your transactions here")

if selected == "Analytics":
    st.header("Analytics")
    fig, ax = plt.subplots()
    categories = ['Rent', 'Food', 'Entertainment', 'Utilities', 'Miscellaneous']
    expense_values = np.random.randint(100, 1000, size=len(categories))
    ax.pie(expense_values, labels=categories, autopct='%1.1f%%')
    st.pyplot(fig)

if selected == "Settings":
    st.header("Settings")
    st.write("Manage your app settings")