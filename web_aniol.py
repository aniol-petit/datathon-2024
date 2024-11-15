import streamlit as st
import pandas as pd
import numpy as np
#Random comment
# Title
st.title("Simple Streamlit App")

# Slider for user input
number = st.slider("Pick a number", 1, 10)

# Display a line chart
data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
st.line_chart(data)

# Show user input
st.write(f"You selected: {number}")
