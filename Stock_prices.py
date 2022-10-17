import yfinance as yf
import streamlit as st
st.write("""
# Simple stock price web application


Shown are the stock closing prices of Tata Motors!

""")


tickerSymbol = 'TTM'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2021-01-01', end='2022-10-11')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
