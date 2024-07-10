import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import datetime as dt
import sqlite3
from PIL import Image
import requests
from io import BytesIO
import base64

# CSS
st.markdown('''
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #f5f5f5;
    color: #333333;
}

.sidebar .sidebar-content {
    background-color: #2e3b4e;
    color: #ffffff;
}

h1, h2, h3, h4, h5, h6 {
    color: #2e3b4e;
}

.stButton>button {
   background-color: #4CAF50;
   color:white;
}

.stButton>button:hover {
   background-color: #45a049;
}

footer {
    visibility: hidden;
}

footer:after {
    content: 'Streamlit App - All Rights Reserved'; 
    visibility: visible;
    display: block;
    position: relative;
    padding: 15px;
    top: 2px;
}
</style>
''', unsafe_allow_html=True)

# Connect to SQLite database
conn = sqlite3.connect('hikes.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS hikes
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            date DATE,
            location TEXT,
            distance REAL,
            duration REAL,
            description TEXT)''')
conn.commit()

# Function to fetch hikes from the database
def get_hikes():
    c.execute('SELECT * FROM hikes')
    data = c.fetchall()
    return pd.DataFrame(data, columns=["ID", "Name", "Date", "Location", "Distance", "Duration", "Description"])

# Function to add hike to the database
def add_hike(name, date, location, distance, duration, description):
    c.execute('INSERT INTO hikes (name, date, location, distance, duration, description) VALUES (?, ?, ?, ?, ?, ?)',
              (name, date, location, distance, duration, description))
    conn.commit()

# Pages
def home():
    st.title("Welcome to Your Hike Tracker!")
    st.image('https://source.unsplash.com/1600x900/?hiking', use_column_width=True)
    intro_text = """ This application helps you discover new hiking trails and record your adventures. Get ready to explore the great outdoors! """
    st.markdown(intro_text)

    if st.button("Find Hikes"):
        st.session_state.page = 'find_hikes'

    if st.button("Record a Hike"):
        st.session_state.page = 'record_hike'

    if st.button("View Recorded Hikes"):
        st.session_state.page = 'view_hikes'

    if st.session_state.page:
        pages[st.session_state.page]()


def find_hikes():
    st.title("Find Hikes")
    location = st.text_input("Enter location:")

    if st.button("Search"):
        # Simulated search
        map_loc = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
        folium.Marker([37.7749, -122.4194], tooltip='Cool Hike 1').add_to(map_loc)
        folium.Marker([37.7849, -122.4294], tooltip='Cool Hike 2').add_to(map_loc)
        folium_static(map_loc)

    if st.button("Back to Home"):
        st.session_state.page = 'home'
        home()


def record_hike():
    st.title("Record a Hike")
    name = st.text_input("Hike Name:")
    date = st.date_input("Date:", dt.date.today())
    location = st.text_input("Location:")
    distance = st.number_input("Distance (km):", min_value=0.0, format="%.1f")
    duration = st.number_input("Duration (hours):", min_value=0.0, format="%.1f")
    description = st.text_area("Description:")

    if st.button("Submit"):
        add_hike(name, date, location, distance, duration, description)
        st.success("Hike Recorded Successfully!")

    if st.button("Back to Home"):
        st.session_state.page = 'home'
        home()


def view_hikes():
    st.title("View Recorded Hikes")

    hikes_df = get_hikes()
    st.dataframe(hikes_df)

    if st.button("Back to Home"):
        st.session_state.page = 'home'
        home()

# Navigation
pages = {
    "home": home,
    "find_hikes": find_hikes,
    "record_hike": record_hike,
    "view_hikes": view_hikes
}

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Load Initial Page
home()