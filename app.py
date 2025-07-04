import streamlit as st
import requests

st.set_page_config(page_title="Gold Price Forecast", page_icon="💰")
st.title("🔮 Gold Price Forecast (XAU/USD)")

# === Fetch gold price using ExchangeRate.host ===
def get_gold_price():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=XAU"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")
    
    data = response.json()
    if 'rates' not in data or 'XAU' not in data['rates']:
        raise Exception("Invalid API response structure.")
    
    xau_per_usd = data['rates']['XAU']
    usd_per_xau = 1 / xau_per_usd
    return usd_per_xau

# === Display price ===
try:
    gold_price = get_gold_price()
    st.metric(label="📈 Live Gold Price (USD/oz)", value=f"${gold_price:.2f}")
except Exception as e:
    st.error("Could not fetch gold price.")
    st.code(str(e))

# === Placeholder for next features ===
st.divider()
st.subheader("📊 Coming Next: Predict Probabilities Based on SL/TP")
st.caption("We’ll soon let you enter Stop Loss / Take Profit levels to calculate win rates.")
