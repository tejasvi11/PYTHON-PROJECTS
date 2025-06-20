import tkinter as tk
from tkinter import messagebox
import requests

api_key = "6937251ec282577c829cccdd935ac147"

def fetch_news():
    query = entry_query.get()
    country = entry_country.get()
    language = entry_language.get()

    if not query:
        messagebox.showwarning("Missing", "Please enter a topic.")
        return

    url = f"https://gnews.io/api/v4/search?q={query}&lang={language}&country={country}&max=5&apikey={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to fetch news.")
        return

    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        messagebox.showinfo("No News", "No articles found for this topic.")
        return

    output.delete("1.0", tk.END)
    for idx, article in enumerate(articles, 1):
        output.insert(tk.END, f"{idx}. {article['title']}\n")
        output.insert(tk.END, f"   Source: {article['source']['name']}\n")
        output.insert(tk.END, f"   Link: {article['url']}\n\n")

def save_to_file():
    content = output.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("No News", "Nothing to save. Please fetch news first.")
        return

    with open("news_gui_output.txt", "w", encoding="utf-8") as f:
        f.write(content)

    messagebox.showinfo("Saved", "News saved to news_gui_output.txt")

# GUI Setup
root = tk.Tk()
root.title("News Aggregator")

tk.Label(root, text="Topic:").grid(row=0, column=0)
entry_query = tk.Entry(root, width=40)
entry_query.grid(row=0, column=1)

tk.Label(root, text="Country (in, us, etc):").grid(row=1, column=0)
entry_country = tk.Entry(root, width=10)
entry_country.insert(0, "in")
entry_country.grid(row=1, column=1, sticky="w")

tk.Label(root, text="Language (en, hi, ja):").grid(row=2, column=0)
entry_language = tk.Entry(root, width=10)
entry_language.insert(0, "en")
entry_language.grid(row=2, column=1, sticky="w")

tk.Button(root, text="Fetch News", command=fetch_news).grid(row=3, columnspan=2, pady=5)
tk.Button(root, text="Save to File", command=save_to_file).grid(row=4, columnspan=2)

output = tk.Text(root, width=80, height=20)
output.grid(row=5, columnspan=2, pady=10)

root.mainloop()
