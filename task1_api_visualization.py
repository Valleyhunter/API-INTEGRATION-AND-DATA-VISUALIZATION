# task1_api_visualization.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 1: Fetch Data from API
# -------------------------------
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",              # Currency in USD
    "order": "market_cap_desc",        # Sort by market cap
    "per_page": 10,                    # Top 10 cryptos
    "page": 1,
    "sparkline": False
}

response = requests.get(url, params=params)

# Check if successful
if response.status_code == 200:
    data = response.json()
else:
    print("Error fetching data:", response.status_code)
    exit()

# -------------------------------
# STEP 2: Convert to DataFrame
# -------------------------------
df = pd.DataFrame(data, columns=["id", "symbol", "current_price", "market_cap", "total_volume"])
print("\nTop 10 Cryptocurrencies:\n", df)

# -------------------------------
# STEP 3: Visualization
# -------------------------------
sns.set(style="whitegrid")

# 1. Market Cap Bar Plot
plt.figure(figsize=(10,6))
sns.barplot(x="id", y="market_cap", hue="id", data=df, palette="viridis", legend=False)
plt.xticks(rotation=45)
plt.title("Top 10 Cryptocurrencies by Market Cap (USD)")
plt.ylabel("Market Cap (in USD)")
plt.xlabel("Cryptocurrency")
plt.tight_layout()
plt.show()

# 2. Current Price Bar Plot
plt.figure(figsize=(10,6))
sns.barplot(x="id", y="current_price", hue="id", data=df, palette="magma", legend=False)
plt.xticks(rotation=45)
plt.title("Top 10 Cryptocurrencies by Current Price (USD)")
plt.ylabel("Price (in USD)")
plt.xlabel("Cryptocurrency")
plt.tight_layout()
plt.show()

# 3. Market Cap vs Volume (Scatter)
plt.figure(figsize=(10,6))
sns.scatterplot(x="market_cap", y="total_volume", hue="id", data=df, s=150, palette="tab10")
plt.title("Market Cap vs Total Volume (Top 10 Cryptos)")
plt.xlabel("Market Cap (USD)")
plt.ylabel("Total Volume (USD)")
plt.legend(title="Crypto", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# -------------------------------
# STEP 4: Save Data
# -------------------------------
df.to_csv("crypto_data.csv", index=False)
print("\nData saved to 'crypto_data.csv'")
