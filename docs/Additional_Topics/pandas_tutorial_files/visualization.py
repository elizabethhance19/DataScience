import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('module://backend_interagg')
# %matplotlib inline # for jupyter notebook to display plot below block

bb = data.DataReader(name="BB", data_source="yahoo", start="2007-01-01", end="2020-12-31")
bb.plot()
bb.plot(y="High")
bb["High"].plot()
bb[["High", "Close"]].plot()

plt.style.available
plt.style.use("fivethirtyeight")
bb.plot(y="Close")


# Bar graph
def rank_performance(stock_price):
    if stock_price <= 10:
        return "Poor"
    elif stock_price <= 50:
        return "Satisfactory"
    else:
        return "Stellar"


plt.style.use("ggplot")
bb["Close"].apply(rank_performance).value_counts().plot(kind="barh")


# Pie Chart
def rank_performance(stock_price):
    if stock_price >= bb["Close"].mean():
        return "Above Average"
    else:
        return "Below Average"


plt.style.use("dark_background")
bb["Close"].apply(rank_performance).value_counts().plot(kind="pie", legend=True)
