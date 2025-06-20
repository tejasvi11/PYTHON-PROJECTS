import requests

API_KEY = "6937251ec282577c829cccdd935ac147"  # ← Replace with your actual GNews API key

BASE_URL = "https://gnews.io/api/v4/top-headlines"
params = {
    'token': API_KEY,
    'lang': 'en',
    'country': 'in',
    'max': 5
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if 'articles' in data and data['articles']:
    print("\n🗞️ Top News Headlines:\n")
    for i, article in enumerate(data['articles'], 1):
        print(f"{i}. {article['title']}")
        print(f"   📰 Source: {article['source']['name']}")
        print(f"   🔗 {article['url']}\n")
else:
    print("❌ No articles found or error occurred.")
    print("Response:", data)
