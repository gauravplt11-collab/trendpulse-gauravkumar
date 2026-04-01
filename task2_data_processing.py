# Task 2: Data Processing
import pandas as pd

# Load data
df = pd.read_csv('trending_data.csv')

# Clean data
df.dropna(inplace=True)
df['Trending'] = df['Trending'].str.lower()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Add length column
df['length'] = df['Trending'].apply(len)

# Save processed data
df.to_csv('processed_data.csv', index=False)

print("Data processed and saved as processed_data.csv")
