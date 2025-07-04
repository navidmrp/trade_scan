import streamlit as st

st.title("🔮 Gold Price Forecast")
st.write("Welcome! This is your first AI-powered trading tool.")

st.subheader("📈 Live Gold/USD Price (coming soon!)")

entry = st.number_input("Enter Entry Price")
sl = st.number_input("Stop Loss")
tp = st.number_input("Take Profit")

# Example output (replace with your model later)
st.write("🧠 Predicted chance of hitting Take Profit: 63%")
st.write("🧠 Predicted chance of hitting Stop Loss: 37%")
