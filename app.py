import streamlit as st
import requests

st.set_page_config(page_title="Gold Price Forecast", page_icon="🔮")
st.title("🔮 Gold Price Forecast (XAU/USD)")

def get_gold_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises error for HTTP 4xx/5xx
        data = response.json()
        price = data["tether-gold"]["usd"]
        return price
    except Exception as e:
        st.error("Could not fetch gold price.")
        st.code(str(e))
        return None

gold_price = get_gold_price()
if gold_price:
    st.metric(label="🪙 Live Gold Price (USD/oz)", value=f"${gold_price:,.2f}")
