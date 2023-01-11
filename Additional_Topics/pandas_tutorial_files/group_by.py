import pandas as pd

fortune = pd.read_csv("fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")

len(sectors)  # number of groupings
sectors.size()  # table of count by group
sectors.first()  # first row in each grouping
sectors.groups  # dictionary with group and index of rows in group

sectors.get_group("Energy")

sectors.max()  # last ranking of first column (Company)
sectors.sum()  # sum all numeric columns
sectors["Revenue"].max()

sectors = fortune.groupby(["Sector", "Industry"])
sectors.size()

# .agg
fortune = pd.read_csv("fortune1000.csv", index_col="Rank")
sectors = fortune.groupby("Sector")
sectors.agg({"Revenue": "sum",
             "Profits": "sum",
             "Employees": "mean"})
sectors.agg(["size", "sum", "mean"])

# iterating through groups
sectors["Profits"].max()  # doesn't show all columns of max rows
df = pd.DataFrame(columns=fortune.columns)
for sector, data in sectors:
    highest_revenue_company_in_group = data.nlargest(1, "Revenue")
    df = df.append(highest_revenue_company_in_group)
df
