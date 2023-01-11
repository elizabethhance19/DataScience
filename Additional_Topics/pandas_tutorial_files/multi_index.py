import pandas as pd

bigmac = pd.read_csv("bigmac.csv", parse_dates=["Date"])

bigmac.set_index(keys=["Date", "Country"], inplace=True)
bigmac.sort_index(inplace=True)


bigmac.index.get_level_values("Date")
bigmac.index.set_names(names=["Day", "Location"])
bigmac.index.set_names(names="Day", level=0)


bigmac.sort_index(ascending=[True, False])

bigmac.loc["2010-01-01", "Argentina"]  # not great because second argument is typically column
bigmac.loc[("2010-01-01", "Argentina")]  # better as a tuple

bigmac.loc[("2010-01-01")]  # multi-index
bigmac.loc[("2010-01-01",)]  # single index

bigmac = bigmac.transpose()
bigmac.loc[("Price in US Dollars",), ('2010-01-01', 'Sri Lanka')]

bigmac = pd.read_csv("bigmac.csv", parse_dates=["Date"], index_col=["Date", "Country"])
bigmac.sort_index(inplace=True)
bigmac.swaplevel()

# Stack/unstack
world = pd.read_csv("worldstats.csv", index_col=["country", "year"])
s = world.stack()  # returns series, similar to pivot_longer
world.stack().to_frame()
s.unstack().unstack()

s.unstack(level=0)
s.unstack(level=[2, 1])
s.unstack("year", fill_value=0)

# Pivot
sales = pd.read_csv("salesmen.csv", parse_dates=["Date"])
sales["Salesman"] = sales["Salesman"].astype("category")
sales.pivot(index="Date", columns="Salesman", values='Revenue')

sales1 = sales.copy()
sales1.set_index(["Date", "Salesman"], inplace=True)
sales1.unstack(1)

# Pivot table
foods = pd.read_csv("foods.csv")
foods.pivot_table(values="Spend", index="Gender", aggfunc="sum")
foods.pivot_table(values="Spend", index=["Gender", "Item"], aggfunc="sum")
foods.pivot_table(values="Spend", index=["Gender", "Item"], columns="City", aggfunc="sum")

# Melt
sales = pd.read_csv("quarters.csv")
pd.melt(sales, id_vars="Salesman", var_name="Quarter", value_name="Revenue")  # pivot longer
