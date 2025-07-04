import streamlit as st
import requests

st.set_page_config(page_title="Gold Price Forecast", page_icon="💰")
st.title("🔮 Gold Price Forecast (XAU/USD)")

# === Live gold price from Yahoo Finance ===
def get_gold_price():
    url = "https://query1.finance.yahoo.com/v8/finance/chart/XAUUSD=X"
    response = requests.get(url)
    data = response.json()
    current_price = data['chart']['result'][0]['meta']['regularMarketPrice']
    return current_price

# Display live price
try:
    gold_price = get_gold_price()
    st.metric(label="📈 Live Gold Price (USD/oz)", value=f"${gold_price:.2f}")
except Exception as e:
    st.error("Could not fetch gold price.")
    st.text(str(e))

# === Optional: Future UI inputs (coming soon) ===
st.divider()
st.subheader("📊 Coming Next: Predict Probabilities Based on SL/TP")
st.caption("We’ll soon let you enter Stop Loss / Take Profit levels to calculate win rates.")

