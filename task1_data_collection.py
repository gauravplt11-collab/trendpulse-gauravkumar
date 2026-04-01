# Task 1: Data Collection
from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(hl='en-IN', tz=330)

# Get trending searches in India
trending = pytrends.trending_searches(pn='india')

# Convert to DataFrame
df = pd.DataFrame(trending, columns=['Trending'])

# Save data
df.to_csv('trending_data.csv', index=False)

print("Data collected and saved as trending_data.csv")
