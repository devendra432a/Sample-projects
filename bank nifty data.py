import yfinance as yf

# Fetch historical data for Banknifty
nifty = yf.Ticker("^NSEBANK")
data = nifty.history(period="max", interval="1mo")

# Save to CSV
data.to_csv("Banknifty.csv")
