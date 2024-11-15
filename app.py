import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Title and Description
st.title("Streamlit Heavy Script Demo")
st.write("This is a comprehensive Streamlit app with various widgets and functionalities.")

# Sidebar
st.sidebar.header("Settings")
name = st.sidebar.text_input("Enter your name:", "Guest")
age = st.sidebar.slider("Select your age:", 0, 100, 25)
st.sidebar.write(f"Hello, {name}. You are {age} years old.")

# Progress Bar
st.write("### Loading Simulation")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.03)  # Simulate a task
    progress.progress(i + 1)
st.write("Loading Complete!")

# Random Data Generation
st.write("### Random Data Visualization")
rows = st.slider("Number of rows to generate:", 10, 1000, 100)
cols = st.slider("Number of columns:", 2, 10, 4)
data = pd.DataFrame(
    np.random.randn(rows, cols),
    columns=[f"Column {i+1}" for i in range(cols)]
)
st.write("Generated Data")
st.dataframe(data)

# Line Chart
st.write("### Line Chart of Random Data")
st.line_chart(data)

# Matplotlib Visualization
st.write("### Matplotlib Plot")
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 4))
plt.plot(x, y, label="sin(x)")
plt.title("Matplotlib Plot: Sine Wave")
plt.legend()
st.pyplot(plt)

# File Upload
st.write("### File Upload")
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded File Data:")
    st.dataframe(df)

# Interactive Filtering
st.write("### Data Filtering")
if uploaded_file:
    column = st.selectbox("Select a column to filter by:", df.columns)
    unique_values = df[column].unique()
    filter_value = st.selectbox("Select a value to filter by:", unique_values)
    filtered_data = df[df[column] == filter_value]
    st.write("Filtered Data:")
    st.dataframe(filtered_data)

# Map Visualization
st.write("### Map Visualization")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)

# End of App
st.write("### End of the App")
st.write("Thanks for trying this heavy Streamlit script!")

