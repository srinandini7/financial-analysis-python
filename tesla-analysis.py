import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. SETTINGS
ticker_symbol = 'TSLA'
start_date = '2023-01-01'
end_date = '2024-01-01'

print(f"Fetching data for {ticker_symbol}...")

# 2. FIXED DATA INGESTION
# auto_adjust=True fixes the 'Adj Close' vs 'Close' issue
df = yf.download(ticker_symbol, start=start_date, end=end_date, auto_adjust=True)

# 3. FIXING THE MULTI-INDEX (Common in new yfinance versions)
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Now we use 'Close' because auto_adjust merged Adj Close into it
# 4. NUMERICAL APTITUDE: The Math Logic
df['Daily_Return'] = df['Close'].pct_change()

# Calculate key metrics
average_daily_return = df['Daily_Return'].mean()
volatility = df['Daily_Return'].std() 
cumulative_return = (1 + df['Daily_Return']).prod() - 1

# 5. COMMUNICATION: Visualizing the Data
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(df['Close'], color='blue', label='Closing Price')
plt.title(f'{ticker_symbol} Performance Analysis (2023)')
plt.ylabel('Price ($)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df['Daily_Return'], color='orange', label='Daily % Change', alpha=0.7)
plt.axhline(0, color='black', lw=1)
plt.ylabel('Daily Return')
plt.legend()

plt.tight_layout()
plt.show()

print("-" * 30)
print(f"ANALYSIS REPORT FOR {ticker_symbol}")
print("-" * 30)
print(f"Total Cumulative Return: {cumulative_return:.2%}")
print(f"Average Daily Return:    {average_daily_return:.4%}")
print(f"Daily Volatility (Risk): {volatility:.2%}")
print("-" * 30)