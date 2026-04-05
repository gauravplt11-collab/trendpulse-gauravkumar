import requests
import json
import os

os.makedirs("data", exist_ok=True)

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
story_ids = response.json()

stories = []

for story_id in story_ids[:150]:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    item_res = requests.get(item_url)
    item = item_res.json()

    if item and "title" in item and "url" in item:
        story = {
            "id": item.get("id"),
            "title": item.get("title"),
            "url": item.get("url"),
            "score": item.get("score"),
            "by": item.get("by"),
            "time": item.get("time"),
            "descendants": item.get("descendants", 0)
        }
        stories.append(story)

    if len(stories) >= 100:
        break

with open("data/top_stories.json", "w") as f:
    json.dump(stories, f, indent=4)

print("Data saved successfully!")