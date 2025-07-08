import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gold Price Forecast", page_icon="🔮")
st.title("🔮 Gold Price Forecast (XAU/USD)")

# Fetch current gold price
def get_gold_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd"
    st.code(f"⛏ Using URL: {url}")
    
    response = requests.get(url, timeout=10)
    st.write("Raw API response:", response.text)

    data = response.json()
    return data["tether-gold"]["usd"]

# Fetch historical gold prices (30 days)
def get_gold_price_history():
    url = "https://api.coingecko.com/api/v3/coins/tether-gold/market_chart?vs_currency=usd&days=30"
    response = requests.get(url)
    data = response.json()

    # Convert to DataFrame
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

# Display current price
try:
    gold_price = g_
