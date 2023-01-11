import pandas as pd

chicago = pd.read_csv("chicago.csv").dropna(how="all")
# chicago.nunique()
chicago["Department"] = chicago["Department"].astype("category")

chicago["Name"].str.lower()
chicago["Department"].str.len()

"Hello world".replace("l", "!")
chicago["Department"] = chicago["Department"].str.replace("MGMNT", "MANAGEMENT")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].str.replace("$", "").astype(float)

chicago["Position Title"].str.lower().str.contains("water")
chicago["Position Title"].str.lower().str.startswith("water")

"    Hello World  ".lstrip()
chicago["Name"].str.lstrip()

chicago = pd.read_csv("chicago.csv", index_col="Name").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.index = chicago.index.str.strip().str.title()

chicago = pd.read_csv("chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
"Hello my name is Elizabeth".split(" ")
chicago["Name"].str.split(",").str.get(0).str.title().value_counts()
chicago["Position Title"].str.split(" ").str.get(0)

chicago["Name"].str.split(",").str.get(1).str.strip().str.split(" ").str.get(0)

chicago[["Last Name", "First Name"]] = chicago["Name"].str.split(",", expand=True)
chicago["Position Title"].str.split(" ", expand=True, n=1)
