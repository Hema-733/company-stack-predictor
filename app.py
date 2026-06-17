import streamlit as st
import yfinance as yf
from groq import Groq

# ==========================
# CONFIG
# ==========================

GROQ_API_KEY = "{YOUR_GROQ_API_KEY}"  # Replace with your actual Groq API key

client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(
    page_title="AI Stock Analyzer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Stock Analyzer")
st.write("Enter a company stock ticker (AAPL, MSFT, TSLA, NVDA, etc.)")

# ==========================
# INPUT
# ==========================

ticker = st.text_input(
    "Enter Stock Ticker",
    placeholder="AAPL"
)

# ==========================
# ANALYSIS
# ==========================

if st.button("Analyze Stock"):

    if not ticker:
        st.warning("Please enter a stock ticker.")
        st.stop()

    try:

        stock = yf.Ticker(ticker)

        info = stock.info

        current_price = info.get("currentPrice", "N/A")
        market_cap = info.get("marketCap", "N/A")
        pe_ratio = info.get("trailingPE", "N/A")
        sector = info.get("sector", "N/A")
        company_name = info.get("longName", ticker)

        hist = stock.history(period="6mo")

        st.success(f"Successfully analyzed {company_name}")

        # ==========================
        # METRICS
        # ==========================

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Current Price", current_price)
        col2.metric("P/E Ratio", pe_ratio)
        col3.metric("Market Cap", f"{market_cap:,}" if isinstance(market_cap, int) else market_cap)
        col4.metric("Sector", sector)

        # ==========================
        # STOCK CHART
        # ==========================

        st.subheader("6 Month Stock Trend")

        st.line_chart(hist["Close"])

        # ==========================
        # AI ANALYSIS
        # ==========================

        with st.spinner("Generating AI stock analysis..."):

            prompt = f"""
You are an expert stock market analyst.

Analyze the following company:

Company: {company_name}

Current Price: {current_price}

Market Cap: {market_cap}

PE Ratio: {pe_ratio}

Sector: {sector}

Provide:

1. Company Summary
2. Bullish Factors
3. Bearish Factors
4. Short-Term Outlook (1-3 Months)
5. Long-Term Outlook (1-3 Years)
6. Risk Level
7. Buy / Hold / Sell Recommendation
8. Confidence Score (%)

Format clearly using markdown.
"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1500
            )

            analysis = response.choices[0].message.content

            st.subheader("🤖 AI Analysis")

            st.markdown(analysis)

    except Exception as e:
        st.error(f"Error: {e}")