import requests

api_key = "6937251ec282577c829cccdd935ac147"

# 🔍 Get user input
query = input("Enter a topic to search news for: ")
country = input("Enter country code (e.g., in, us, jp): ")
language = input("Enter language code (e.g., en, hi, ja): ")

# 🛠️ Build API URL
url = f"https://gnews.io/api/v4/search?q={query}&lang={language}&country={country}&max=5&apikey={api_key}"


response = requests.get(url)
if response.status_code != 200:
    print("❌ Error: Could not fetch news. Check your API key or network.")
    exit()

data = response.json()
if not data.get("articles"):
    print("⚠️ No news articles found for that topic. Try a different one.")
    exit()


# Step 3: Display results
if data.get("totalArticles", 0) > 0:
    print("\n🗞️ Top News Headlines:\n")
    for idx, article in enumerate(data["articles"], 1):
        print(f"{idx}. {article['title']}")
        print(f"   📰 Source: {article['source']['name']}")
        print(f"   🔗 Link: {article['url']}\n")
    # ✍️ Save to file (make sure this is inside your if block!)
    with open("news.txt", "w", encoding="utf-8") as f:
         f.write(f"📰 News on '{query}' (Country: {country}, Language: {language})\n\n")
         for idx, article in enumerate(data["articles"], 1):
             f.write(f"{idx}. {article['title']}\n")
             f.write(f"   Source: {article['source']['name']}\n")
             f.write(f"   Link: {article['url']}\n\n")

    print("✅ News saved to news.txt")
   
else:
     print("⚠️ No articles found or something went wrong.")

