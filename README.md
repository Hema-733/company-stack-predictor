# 📈 AI Stock Analyzer

An AI-powered stock analysis application built using **Streamlit**, **Groq**, and **Yahoo Finance**.

The application allows users to enter a stock ticker symbol and receive real-time stock information along with AI-generated market insights, risk analysis, and investment recommendations.

---

## 🚀 Features

- Real-time stock market data retrieval
- Company information lookup
- Historical stock price visualization
- AI-generated stock analysis
- Short-term and long-term outlook
- Risk assessment
- Buy / Hold / Sell recommendation
- Interactive Streamlit dashboard

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Streamlit | User Interface |
| Groq API | AI-powered analysis |
| Llama 3.3 70B | Large Language Model |
| Yahoo Finance (yfinance) | Real-time stock data |
| Pandas | Data processing and manipulation |

---

## 📂 Project Structure

```text
company-stack-predictor/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/company-stack-predictor.git
cd company-stack-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Open `app.py` and replace:

```python
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

with your actual Groq API key.

Get your API key from:

https://console.groq.com

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📊 Example Usage

### Input

```text
AAPL
```

### Output

- Current Stock Price
- Market Capitalization
- PE Ratio
- Historical Price Chart
- AI Analysis
- Risk Assessment
- Buy / Hold / Sell Recommendation

---

## 🔄 Workflow

```text
User Input
     │
     ▼
Yahoo Finance
     │
     ▼
Stock Data Collection
     │
     ▼
Groq AI Analysis
     │
     ▼
Investment Insights
     │
     ▼
Streamlit Dashboard
```

---

## 📦 Requirements

```txt
streamlit
groq
yfinance
pandas
```

---


## 👩‍💻 Author

**Hema Varshana**

Computer Science Engineering Student

Interested in AI, Full Stack Development.

---

## 📄 License

This project is intended for educational, learning, and portfolio purposes.
