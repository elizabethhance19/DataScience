import pandas as pd

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
foods = pd.read_csv("Restaurant - Foods.csv")

pd.concat(objs=[week1, week2], ignore_index=True)  # make new index
week1.append(other=week2, ignore_index=True)  # identical to pd.concat

sales = pd.concat(objs=[week1, week2], keys=["Week 1", "Week 2"])  # multi-index
sales.loc[("Week 1",)]  # gives week1

# Inner join
week1.merge(week2, how="inner", on='Customer ID', suffixes=[" - Week 1", " - Week 2"])
week1.merge(week2, on=['Customer ID', 'Food ID'])
week1[week1["Customer ID"] == 21]  # came twice first week and bought same thing
week2[week2["Customer ID"] == 21]

# Outer join
merged = week1.merge(week2, how="outer", on="Customer ID", suffixes=[" - Week 1", " - Week 2"],
                     indicator=True)
merged["_merge"].value_counts()
mask = merged["_merge"].isin(["left_only", "right_only"])
merged[mask]  # remove overlap between left and right

# Left join
week1.merge(foods, how="left", on="Food ID", sort=True)  # sort on matching column

# Different column names
week2.merge(customers, how="left", left_on="Customer ID", right_on="ID").drop("ID", axis=1)

# Merge using index
customers = pd.read_csv("Restaurant - Customers.csv", index_col="ID")
foods = pd.read_csv("Restaurant - Foods.csv", index_col="Food ID")
sales = week1.merge(customers, how="left", left_on="Customer ID", right_index=True)
sales.merge(foods, how="left", left_on="Food ID", right_index=True)

week1.merge(week2, how="left", left_index=True, right_index=True)

# .join(), like cbind
satisfaction = pd.read_csv("Restaurant - Week 1 Satisfaction.csv")
week1.merge(satisfaction, how="left", left_index=True, right_index=True)
week1.join(satisfaction)

pd.merge(week1, customers, how="left", left_on="Customer ID", right_on="ID")
