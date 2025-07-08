import streamlit as st
import requests

st.set_page_config(page_title="Gold Price Forecast", page_icon="🔮")
st.title("🔮 Gold Price Forecast (XAU/USD)")

def get_gold_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd"
    st.code(f"⛏ Using URL: {url}")
    
    response = requests.get(url, timeout=10)
    st.write("Raw API response:", response.text)

    data = response.json()
    if "tether-gold" not in data:
        raise Exception("Invalid API response structure.")

    xau_price = data["tether-gold"]["usd"]
    return xau_price

try:
    gold_price = get_gold_price()
    st.metric(label="🪙 Live Gold Price (USD/oz)", value=f"${gold_price:.2f}")
except Exception as e:
    st.error("Could not fetch gold price.")
    st.code(str(e))

st.divider()
st.subheader("📊 Coming Next: Predict Probabilities Based on SL/TP")
st.caption("We’ll soon let you enter Stop Loss / Take Profit levels to calculate win rates.")
