# Task 1: Data Collection (No API - Stable Version)
import pandas as pd

# Sample trending topics (simulated data)
trending_topics = [
    "IPL 2026",
    "Election News",
    "Stock Market",
    "Cricket मैच",
    "Weather Update",
    "AI Technology",
    "Bollywood News",
    "Startup India",
    "Gold Price",
    "Bitcoin"
]

# Convert to DataFrame
df = pd.DataFrame(trending_topics, columns=['Trending'])

# Save data
df.to_csv('trending_data.csv', index=False)

print("Data collected successfully (static data)")
