import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Title
st.set_page_config(page_title="Gold Price Forecast", page_icon="🔮")
st.title("🔮 Gold Price Forecast (XAU/USD)")

# 🟢 1. Get Live Price
def get_live_gold_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["tether-gold"]["usd"]

# 🟢 2. Get historical prices (last 365 days)
def get_gold_price_history():
    url = "https://api.coingecko.com/api/v3/coins/tether-gold/market_chart?vs_currency=usd&days=365"
    response = requests.get(url)
    data = response.json()
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df[["date", "price"]]

# 🔵 Display price metric
try:
    price = get_live_gold_price()
    st.markdown(f"<h2 style='font-size: 60px; color: #333;'>💵 ${price:,.2f}</h2>", unsafe_allow_html=True)
except:
    st.error("Could not fetch live gold price.")

# 🔵 Display historical chart
try:
    df = get_gold_price_history()
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["price"], linewidth=2)
    ax.set_title("📉 Gold Price (Last 365 Days)", fontsize=16)
    ax.set_ylabel("Price (USD)")
    ax.set_xlabel("Date")

    # 🟢 Custom Y-axis: do not start at zero
    ymin = df["price"].min() * 0.98
    ymax = df["price"].max() * 1.02
    ax.set_ylim(ymin, ymax)

    st.pyplot(fig)
except:
    st.error("Could not load gold price history.")
