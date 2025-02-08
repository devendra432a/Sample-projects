import yfinance as yf

# Fetch historical data for Nifty 50
nifty = yf.Ticker("^NSEI")
data = nifty.history(period="max", interval="1mo")

# Save to CSV
data.to_csv("nifty_50_monthly.csv")
