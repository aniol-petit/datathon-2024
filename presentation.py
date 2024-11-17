import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Introduction
st.title("🏡 House Price Prediction Project")
st.header("Data Cleaning and Model Performance")

st.markdown("""
Welcome to our project presentation. Our focus is on demonstrating the data cleaning and preprocessing steps
that we undertook to prepare the dataset for modeling. We'll also showcase the model's performance on the training data.
""")

# Section 1: Data Cleaning and Preprocessing
st.subheader("📊 Data Cleaning and Preprocessing")
st.markdown("""
This phase was crucial for ensuring that the dataset was ready for modeling. Key steps included:
- **Handling Missing Values:** Replaced with appropriate measures (e.g., mean, median, or mode).
- **Outlier Detection and Treatment:** Used techniques like IQR to remove or cap extreme values.
- **Feature Engineering:** Created new features to enhance predictive power.
- **Normalization/Standardization:** Scaled numerical features for better model performance.
""")

# Example Visualization: Distribution before and after cleaning
st.markdown("### Example: Feature Distribution Before and After Cleaning")

# Replace this with your actual data
raw_data = {
    "Square Footage": [500, 1000, 2000, 3000, 10000, 50000],
    "Price": [50000, 100000, 200000, 300000, 1000000, 5000000],
}
cleaned_data = {
    "Square Footage": [500, 1000, 2000, 3000, 5000, 5000],  # Example of capping extreme values
    "Price": [50000, 100000, 200000, 300000, 500000, 500000],  # Example of capping
}

df_raw = pd.DataFrame(raw_data)
df_cleaned = pd.DataFrame(cleaned_data)

# Create subplots to compare raw and cleaned data
fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
sns.histplot(df_raw["Price"], bins=10, kde=True, ax=axes[0], color="skyblue")
axes[0].set_title("Raw Data: Price Distribution")

sns.histplot(df_cleaned["Price"], bins=10, kde=True, ax=axes[1], color="lightgreen")
axes[1].set_title("Cleaned Data: Price Distribution")

st.pyplot(fig)

# Section 2: EDA (Exploratory Data Analysis)
st.subheader("📈 Exploratory Data Analysis (EDA)")
st.markdown("""
EDA helped us understand the dataset and identify relationships between features. For example:
""")

# Replace with your actual dataset
correlation_matrix = pd.DataFrame({
    "Square Footage": [1.0, 0.85],
    "Price": [0.85, 1.0],
}, index=["Square Footage", "Price"])

st.markdown("### Correlation Matrix")
st.write(correlation_matrix)

# Add heatmap
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Section 3: Model Performance
st.subheader("🤖 Model Performance on Training Data")
st.markdown("""
After preprocessing the data, we trained a machine learning model and evaluated its performance using the following metrics:
""")

# Example metrics
performance_metrics = pd.DataFrame({
    "Metric": ["Mean Absolute Error (MAE)", "Root Mean Squared Error (RMSE)", "R² Score"],
    "Value": [30000, 40000, 0.90],  # Replace with your actual values
})
st.table(performance_metrics)

st.markdown("""
We achieved a strong **R² score** of 0.90, indicating that our model explains 90% of the variance in house prices 
based on the input features.
""")

# Example: Actual vs. Predicted Prices Visualization
st.markdown("### Actual vs. Predicted Prices (Training Data)")
# Replace with your actual data
actual_vs_predicted = pd.DataFrame({
    "Actual": [100000, 200000, 300000, 400000, 500000],
    "Predicted": [110000, 195000, 305000, 390000, 510000],
})

fig, ax = plt.subplots()
sns.scatterplot(x="Actual", y="Predicted", data=actual_vs_predicted, ax=ax, color="blue")
ax.plot([100000, 500000], [100000, 500000], "r--")  # Reference line
ax.set_title("Actual vs. Predicted Prices")
st.pyplot(fig)

# Footer
st.markdown("### Thank you for your attention! Feel free to ask any questions.")
