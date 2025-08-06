import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Page title
st.title("Nifty Stock Price Visualization")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("../Nifty_Stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Category selection
categories = df['Category'].unique()
selected_category = st.selectbox("Select a Category", categories)

# Filter symbols for selected category
filtered_by_category = df[df['Category'] == selected_category]
symbols = filtered_by_category['Symbol'].unique()
selected_symbol = st.selectbox("Select a Symbol", symbols)

# Filter by selected symbol
filtered_data = filtered_by_category[filtered_by_category['Symbol'] == selected_symbol]

# Line plot using Seaborn
st.subheader(f"Closing Price Trend: {selected_symbol}")

fig, ax = plt.subplots(figsize=(15, 6))
sb.lineplot(x=filtered_data['Date'], y=filtered_data['Close'], ax=ax)
ax.set_title(f"{selected_symbol} Stock Closing Price Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Closing Price")
st.pyplot(fig)
