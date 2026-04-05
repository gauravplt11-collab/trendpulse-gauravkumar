import pandas as pd
import numpy as np

# -------------------------------
# Step 1: Load the CSV file
# -------------------------------
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print(f"Loaded {len(df)} rows from {file_path}")

# Explore data
print("\nFirst 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)


# -------------------------------
# Step 2: NumPy Statistics
# -------------------------------
# Calculate statistics on score

scores = df["score"].values

print("\nStatistics:")
print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))


# -------------------------------
# Step 3: Add New Columns
# -------------------------------

# 1. Score Category (low / medium / high)
def score_category(score):
    if score < 50:
        return "low"
    elif score < 150:
        return "medium"
    else:
        return "high"

df["score_category"] = df["score"].apply(score_category)


# 2. Engagement score (score + comments)
df["engagement"] = df["score"] + df["num_comments"]


# -------------------------------
# Step 4: Save to new CSV
# -------------------------------
output_path = "data/trends_analysed.csv"

df.to_csv(output_path, index=False)

print(f"\nData saved to {output_path}")


# -------------------------------
# Bonus: Category summary
# -------------------------------
print("\nScore category counts:")
print(df["score_category"].value_counts())