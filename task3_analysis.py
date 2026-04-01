# Task 3: Analysis
import pandas as pd

# Load processed data
df = pd.read_csv('processed_data.csv')

# Basic analysis
total_trends = len(df)
avg_length = df['length'].mean()
longest_trend = df.loc[df['length'].idxmax()]

print("Total Trends:", total_trends)
print("Average Length:", avg_length)
print("Longest Trend:", longest_trend['Trending'])

# Save summary
summary = pd.DataFrame({
    "Total Trends": [total_trends],
    "Average Length": [avg_length],
    "Longest Trend": [longest_trend['Trending']]
})

summary.to_csv('analysis_summary.csv', index=False)
