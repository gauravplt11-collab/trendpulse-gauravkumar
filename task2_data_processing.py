# Task 2 — Clean the Data & Save as CSV
# TrendPulse Project
# Author: Gaurav Kumar

import pandas as pd
import os

# Step 1: Load JSON file
file_path = "data/top_stories.json"   # change date if needed

# Check if file exists
if not os.path.exists(file_path):
    print("File not found:", file_path)
    exit()

# Load JSON into DataFrame
df = pd.read_json(file_path)

# Print total rows loaded
print(f"Loaded {len(df)} stories from {file_path}")
# 🔥 FIX (ADD THIS)
df = df.rename(columns={
    "id": "post_id",
    "descendants": "num_comments"
}
)
# -------------------------------
# Step 2: Clean the Data
# -------------------------------

# Remove duplicates based on post_id
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove rows with missing important fields
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert score and num_comments to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Remove extra whitespace from title
df["title"] = df["title"].str.strip()

# -------------------------------
# Step 3: Save Cleaned Data
# -------------------------------

output_path = "data/trends_clean.csv"
# 🔥 ADD THIS LINE
df["category"] = "technology"
# Save to CSV
df.to_csv(output_path, index=False)

# Print confirmation
print(f"\nSaved {len(df)} rows to {output_path}")

# -------------------------------
# Summary: Stories per category
# -------------------------------

print("\nStories per category:")
print(df["category"].value_counts())