import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Step 1: Load Data & Setup
# -------------------------------

file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

print(f"Loaded {len(df)} rows")

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)


# -------------------------------
# Step 2: Chart 1 - Top 10 Stories by Score
# -------------------------------

# Sort and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten titles (max 50 chars)
top10["short_title"] = top10["title"].apply(lambda x: x[:50])

plt.figure()

plt.barh(top10["short_title"], top10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()  # highest on top

plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# -------------------------------
# Step 3: Chart 2 - Stories per Category
# -------------------------------

category_counts = df["category"].value_counts()

plt.figure()

plt.bar(category_counts.index, category_counts.values)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()


# -------------------------------
# Step 4: Chart 3 - Scatter Plot
# -------------------------------

# Create is_popular column if not exists
if "is_popular" not in df.columns:
    df["is_popular"] = df["score"] > 100

# Separate data
popular = df[df["is_popular"] == True]
non_popular = df[df["is_popular"] == False]

plt.figure()

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(non_popular["score"], non_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()


# -------------------------------
# Bonus: Dashboard
# -------------------------------

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top Stories")
axes[0].invert_yaxis()

# Chart 2
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")

# Chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(non_popular["score"], non_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

# Overall title
plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs folder!")