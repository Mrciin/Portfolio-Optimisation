import yfinance as yf
import streamlit as st

print("✅ Libraries imported successfully!")

# Try fetching 1 day of Apple data
data = yf.download("AAPL", period="1d")
print(f"✅ Data fetch successful: {len(data)} rows retrieved.")