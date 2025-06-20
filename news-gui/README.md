Here’s a clean and complete `README.md` just for your **News Aggregator GUI** project:

---

### 📄 `news-gui/README.md`

````markdown
# 🗞️ News Aggregator GUI

A simple Python GUI application that fetches the latest news headlines based on user input using the [GNews API](https://gnews.io/). Built with Tkinter for the interface, this project helps users get real-time news and save the results locally.

---

## 🔧 Features

- Search news by topic (e.g., technology, sports)
- Set preferred language and country (e.g., en/in)
- View top 5 headlines
- Save news results to a `.txt` file with one click

---

## 🛠️ Technologies Used

- Python 3.11+
- Tkinter (for GUI)
- Requests (for API calls)
- GNews API

---

## ▶️ How to Run

1. Install dependencies (if needed):
   ```bash
   pip install requests
````

2. Open terminal in the `news-gui` folder and run:

   ```bash
   python news_gui.py
   ```

3. Enter a topic, country code (`in`, `us`, `jp`, etc.), and language code (`en`, `hi`, etc.), then click **Fetch News**.

---

## 🔑 API Key Setup

* Get your free API key from [gnews.io](https://gnews.io/)
* Open `news_gui.py` and paste your key:

  ```python
  api_key = "your_api_key_here"
  ```

---

## 💾 Output

* News headlines will be shown in the app window
* Click **Save to File** to export results to `news_gui_output.txt`

---

## 🧠 Created By

**Tejasvi Pakala**
[GitHub Profile](https://github.com/tejasvi11)
