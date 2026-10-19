# 📈 Stock News Alert

An automated Python application that monitors **IBM stock price movements** using the **Alpha Vantage API** and sends the latest **news headlines via SMS** using the **Twilio API** whenever the stock price changes significantly. The application helps users stay informed about important market movements without manually checking stock prices or financial news.

![Python](https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white) ![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=plastic) ![Twilio](https://img.shields.io/badge/Twilio-F22F46?style=plastic&logo=twilio&logoColor=white) ![Alpha Vantage](https://img.shields.io/badge/Alpha_Vantage-0066CC?style=plastic) ![News API](https://img.shields.io/badge/News_API-0088CC?style=plastic) ![REST API](https://img.shields.io/badge/REST_API-009688?style=plastic) ![JSON](https://img.shields.io/badge/JSON-000000?style=plastic&logo=json) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=plastic&logo=visualstudiocode&logoColor=white)

---

## ✨ Features

- 📊 Fetches daily stock prices from Alpha Vantage API
- 📈 Calculates daily percentage change in stock price
- 🔺 Detects stock price increase or decrease
- 📰 Retrieves the latest news articles related to the company
- 📩 Sends SMS notifications using Twilio API
- 📄 Includes headline and brief description of each news article
- ⚡ Sends alerts only when the price movement exceeds a predefined threshold
- 🔐 Keeps API keys separate for easy configuration

---

## 📂 Project Structure

```text
23_Stock_News_Alert/
│
├── Stock_News.py          # Main application
│
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- Requests
- Twilio API
- Alpha Vantage API
- News API

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Harsh-Belekar/Python-Projects.git

# Navigate to the project
cd 23_Stock_News_Alert
```

### 2️⃣ Install Required Library

```bash
pip install requests twilio
```

### 3️⃣ Configure Credentials

Replace the placeholder values in **Stock_News.py**:

```python
account_SID="your_account_SID"
auth_token="your_auth_token"

stock_aip_key="your_stock_API_Key"
news_api_key="your_news_API_Key"
```

Also replace:

```python
my_phone_number
Twilio phone number
```

with your own values.

### 4️⃣ Run the Program

```bash
python Stock_News.py
```

---

## ⚙️ How It Works

1. Connects to the Alpha Vantage Stock API.
2. Retrieves the latest two days of IBM stock prices.
3. Calculates the percentage difference.
4. Determines whether the stock price increased or decreased.
5. If the change exceeds **5%**, the application:
   - Connects to the News API.
   - Fetches the latest news articles.
   - Selects the top three articles.
6. Formats each article into a readable SMS.
7. Sends the news directly to your phone using Twilio.

---

## 📂 Source File

| File | Description |
|------|-------------|
| **Stock_News.py** | Fetches stock prices, retrieves news articles, calculates stock movement, and sends SMS alerts. |

---

## 🌐 APIs Used

### 📊 Alpha Vantage API

Used to retrieve daily stock market data.

Features:

- Daily stock prices
- Historical market data
- Percentage change calculation

---

### 📰 News API

Used to fetch the latest company-related news.

Features:

- Company news search
- Headlines
- Article summaries

---

### 📱 Twilio API

Used to send SMS notifications.

Features:

- SMS messaging
- Real-time alerts
- Cloud communication service

---

## 📚 Concepts Practiced

- REST API Integration
- JSON Parsing
- HTTP Requests
- Percentage Calculations
- Conditional Logic
- SMS Automation
- Working with External APIs
- List Comprehensions
- String Formatting
- Python Requests Library

---

## 🎓 Learning Outcomes

Through this project, I learned:

- How to work with multiple APIs in a single application.
- Fetching and processing real-time stock market data.
- Parsing JSON responses from REST APIs.
- Automating SMS notifications using Twilio.
- Working with financial data.
- Filtering and formatting news articles.
- Building real-world automation projects in Python.
- Handling API authentication securely.

---

## 🔒 Security Note

This project contains placeholder values for:

- Alpha Vantage API Key
- News API Key
- Twilio Account SID
- Twilio Auth Token
- Phone Numbers

Never commit your actual credentials to GitHub. Store sensitive information using environment variables or a `.env` file.

---

# 📂 More Projects

This project is part of my **Python Projects Portfolio**, a collection of Python projects covering:

- 🎮 Games
- 🎨 Graphics Programming
- 🖥️ GUI Applications
- 🤖 Automation
- 🌐 API Integrations
- 📊 Data Processing
- 🧩 Python Fundamentals

*Explore the repository to discover more projects and follow my Python learning journey.*

***⭐ If you like this project, don't forget to star the repository!***