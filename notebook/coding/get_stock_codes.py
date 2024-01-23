# filename: get_stock_codes.py
import tushare as ts

# 获取1999年中国A股的股票代码列表
stocks = ts.get_stock_basics()
stocks_1999 = stocks[stocks["timeToMarket"].apply(lambda x: str(x)[:4]) == "1999"]
stock_codes = stocks_1999.index.tolist()

# 打印股票代码列表
print(stock_codes)
