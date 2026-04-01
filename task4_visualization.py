# Task 4: Visualization
import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv('processed_data.csv')

# Plot trend lengths
plt.figure()
df['length'].plot(kind='bar')

plt.title("Length of Trending Topics")
plt.xlabel("Index")
plt.ylabel("Length")

# Save plot
plt.savefig("trend_visualization.png")

print("Visualization saved as trend_visualization.png")
