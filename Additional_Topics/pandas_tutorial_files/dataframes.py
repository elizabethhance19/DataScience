import pandas as pd

# Introduction
nba = pd.read_csv("nba.csv")

nba.values
nba.shape
nba.dtypes.value_counts()
nba.columns
nba.info()

rev = pd.read_csv("revenue.csv", index_col="Date")
s = pd.Series([1, 2, 3])
s.sum()
rev.sum()
rev.sum(axis=1)  # axis = "columns"

nba.Name[1]
nba["Name"][1]
nba[["Name", "Team"]]

nba["Sport"] = "Basketball"
nba.insert(3, column="League", value="NBA")

nba["Age"].add(5)
nba["Age"] + 5
nba.Team.value_counts()

nba.dropna()  # drop any rows with 1+ null value
nba.dropna(how="all")
nba.dropna(subset=["Salary"])  # drop rows where salary is null
nba.Salary.fillna(0, inplace=True)
nba.College.fillna("No College", inplace=True)

nba = pd.read_csv("nba.csv").dropna(how="all")
nba.Salary.fillna(0, inplace=True)
nba.College.fillna("No College", inplace=True)
nba.dtypes
nba.Salary = nba.Salary.astype("int")
nba.Position.nunique()
nba.Position = nba.Position.astype("category")

nba.sort_values("Name")
nba.sort_values(["Team", "Name"], ascending=[True, False], inplace=True)
nba.sort_index()

nba = pd.read_csv("nba.csv").dropna(how="all")
nba.Salary = nba.Salary.fillna(0).astype("int")
nba["Salary Rank"] = nba.Salary.rank(ascending=False).astype("int")  # highest salary has lowest rank

# Filtering
df = pd.read_csv("employees.csv", parse_date=["Start Date", "Last Login Time"])
# df["Start Date"] = pd.to_datetime(df["Start Date"])
# df["Last Login Time"] = pd.to_datetime(df["Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")

df[df["Gender"] == "Male"]
df[df["Team"].isin(["Legal", "Sales", "Product"])]

df["Team"].isnull()
df["Salary"].between(60000, 70000)
df["Start Date"].between("1991-01-01", "1992-01-01")
df["Last Login Time"].between("8:30AM", "12:00PM")

df["First Name"].duplicated()
~df["First Name"].duplicated(keep=False)  # all rows with non-duplicated names

df.drop_duplicates(subset="First Name", keep=False)

df["Gender"].unique()
df["Team"].nunique()  # doesn't count nan

# Data Extraction
bond = pd.read_csv("jamesbond.csv")
bond.set_index(keys="Film", inplace=True)  # can have duplicate names for index
bond.reset_index(inplace=True)
bond.set_index("Film", inplace=True)
bond.reset_index().set_index("Year")

bond = pd.read_csv("jamesbond.csv", index_col="Film")
bond.sort_index(inplace=True)
bond.loc["Goldfinger"]
bond.loc["Diamonds Are Forever":"From Russia with Love"]  # right inclusive
"Gold Bond" in bond.index
bond.iloc[1]
bond.iloc[4:8]  # right non-inclusive

bond.loc["Moonraker", "Actor"]
bond.loc["Moonraker"][1]
bond.loc["Moonraker", ["Director", "Box Office"]]
bond.iloc[14, 2]

bond.loc["Dr. No", "Actor"] = "Sir Sean Connery"
bond.loc["Dr. No", ["Box Office", "Budget", "Bond Actor Salary"]] = [450, 70, 6]

# bond[ bond["Actor"] == "Sean Connery" ]["Actor"] = "Sir Sean Connery" #doesn't work because makes copy of subset of df
bond.loc[bond["Actor"] == "Sean Connery", "Actor"] = "Sir Sean Connery"

bond.rename(mapper={"GoldenEye": "Golden Eye"})  # rename row axis labels
bond.rename(mapper={"Year": "Release Date"}, axis=1)
bond.rename(columns={"Year": "Release Date"})
bond.columns = ['Year of Release', "Actor", "Director", "Gross", 'Cost', 'Salary']

bond.drop("A View to a Kill")
bond.drop("Box Office", axis=1)
bond.pop("Actor")
del bond["Director"]

bond.sample(n=5)
bond.nlargest(3, "Box Office")
bond["Box Office"].nlargest(3)

mask = bond["Actor"] == "Sean Connery"
bond[mask]
bond.where(mask)

bond.columns = [column_name.replace(" ", "_") for column_name in bond.columns]
bond.query('Actor == "Sean Connery"')
bond.query("Actor == 'Roger Moore' and Director == 'John Glen'")


def convert_to_string_and_add_millions(number):
    return str(number) + " MILLIONS!"


bond["Box Office"].apply(convert_to_string_and_add_millions)


def good_movie(row):
    actor = row[1]
    budget = row[4]
    if actor == 'Pierce Brosnan':
        return 'The best'
    elif actor == "Roger Moore" and budget > 40:
        return "Enjoyable"
    else:
        return "I have no clue"


bond.apply(good_movie, axis="columns")

directors = bond["Director"]
directors["A View to a Kill"] = "Mister John Glen"  # error, overwrites in dataframe
directors = bond["Director"].copy()
directors["A View to a Kill"] = "Mister John Glen"  # doesn't overwrite
