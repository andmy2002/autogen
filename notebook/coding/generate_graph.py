# filename: generate_graph.py

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# 获取当前年份
year = pd.Timestamp.now().year

# 获取工商银行(ICBC)的历史数据
icbc = yf.Ticker("601398.SS")  # SS表示上海证券交易所，如果是深圳证券交易所，则更改为SZ

# 获取ICBC的年初至今的价格数据(YTD)
hist = icbc.history(start=f"{year}-01-01")

# 生成图形
plt.figure(figsize=(14, 7))
plt.plot(hist.index, hist["Close"])
plt.title("ICBC Stock Price Change Year to Date (YTD)")
plt.ylabel("Price (CNY)")
plt.grid(True)
plt.savefig("stock_price_ytd.png")
