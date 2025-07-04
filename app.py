import streamlit as st
import requests

st.set_page_config(page_title="Gold Price Forecast", page_icon="💰")
st.title("🔮 Gold Price Forecast (XAU/USD)")

# === Working gold price fetch ===
def get_gold_price():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=XAU"
    response = requests.get(url)
    data = response.json()
    rate = data['rates']['XAU']
    return 1 / rate  # Converts from XAU per USD to USD per XAU

# Display live price
try:
    gold_price = get_gold_price()
    st.metric(label="📈 Live Gold Price (USD/oz)", value=f"${gold_price:.2f}")
except Exception as e:
    st.error("Could not fetch gold price.")
    st.text(str(e))

st.divider()
st.subheader("📊 Coming Next: Predict Probabilities Based on SL/TP")
st.caption("We’ll soon let you enter Stop Loss / Take Profit levels to calculate win rates.")
