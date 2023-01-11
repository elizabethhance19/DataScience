import pandas as pd
import datetime as dt

someday = dt.date(2016, 4, 12)
someday.year
str(dt.datetime(2010, 1, 20, 8))

pd.Timestamp("2015-03-31")
pd.Timestamp("2015/03/31")
pd.Timestamp("2013, 11, 04")
pd.Timestamp("1/1/2015")
pd.Timestamp("19/12/2015")
pd.Timestamp("2021-03-08 08:25:16")
pd.Timestamp(dt.datetime(2015, 1, 1))

dates = ["2016-01-02", "2016-04-12", "2009-09-07"]
pd.DatetimeIndex(dates)
dates = [dt.date(2016, 1, 10), dt.date(1994, 6, 13), dt.date(2003, 12, 29)]

dtIndex = pd.DatetimeIndex(dates)
values = [100, 200, 300]
pd.Series(data=values, index=dtIndex)

# pd.to_datetime()
pd.to_datetime("2001-04-19")
pd.to_datetime(["2015-01-03", "2014/02/08", "2016", "July 4th, 1996"])

times = pd.Series(["2015-01-03", "2014/02/08", "2016", "July 4th, 1996"])  # series with strings
pd.to_datetime(times)  # series with time stamps

dates = pd.Series(["July 4th, 1996", "10/04/1991", "Hello", "2015-02-31"])
pd.to_datetime(dates)  # error
pd.to_datetime(dates, errors="coerce")  # NaT not a time for problems

# pd.date_range()
pd.date_range(start="2016-01-01", end="2016-01-10", freq="D")
pd.date_range(start="2016-01-01", end="2016-01-10", freq="2D")
pd.date_range(start="2016-01-01", end="2016-01-10", freq="B")  # business days
pd.date_range(start="2016-01-01", end="2016-01-10", freq="W")  # week with Sunday as start

pd.date_range(start="2012-09-09", periods=25)  # 25 days after start

pd.date_range(end="1999-12-31", periods=20, freq="D")  # 20 days before end

# .dt
bunch_of_dates = pd.date_range(start="2000-01-01", end="2010-12-31", freq="24D")  # datetime object
s = pd.Series(bunch_of_dates)  # pandas series
bunch_of_dates.day
s.dt.day
s.dt.weekday
s.dt.day_name()
s.dt.is_quarter_start

# pandas_datareader
from pandas_datareader import data

stocks = data.DataReader(name="MSFT", data_source="yahoo", start="2010-01-01", end="2020-12-31")
stocks.loc["2010-01-04"]
stocks.loc[pd.Timestamp("2010-01-04")]
stocks.iloc[0]
stocks.loc[["2010-01-04", "2010-01-05"]]  # might fail
stocks.loc[[pd.Timestamp("2010-01-04"), pd.Timestamp("2010-01-05")]]  # better
stocks.loc["2013-10-01":"2013-10-07"]
stocks.truncate(before="2013-10-01", after="2013-10-07")
birthdays = pd.date_range(start="1991-04-12", end="2020-12-31", freq=pd.DateOffset(years=1))
stocks[stocks.index.isin(birthdays)]

someday = stocks.index[500]
someday.month
someday.month_name()
stocks.index.day_name()
stocks.insert(0, "Day of Week", stocks.index.day_name())
stocks

# pd.DateOffset
stocks.index + 5  # error
stocks.index + pd.DateOffset(days=5)

# Timeseries offsets
stocks.index + pd.tseries.offsets.MonthEnd()  # round to end of month, but 4/30 -> 5/31
from pandas.tseries import offsets

stocks.index + offsets.MonthEnd()  # shortcut

# Timedelta
time_a = pd.Timestamp("2020-03-31")
time_b = pd.Timestamp("2020-03-20")
time_a - time_b
time_b - time_a
time_a + pd.Timedelta(days=3)
pd.Timedelta(days=3, hours=12)
pd.Timedelta("6 hours 12 minutes")

shipping = pd.read_csv("ecommerce.csv", index_col="ID", parse_dates=["order_date", "delivery_date"])
shipping["Delivery Time"] = shipping.delivery_date - shipping.order_date
shipping.delivery_date + shipping["Delivery Time"]
