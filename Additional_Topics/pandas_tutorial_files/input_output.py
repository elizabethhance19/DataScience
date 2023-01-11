import pandas as pd

baby_names = pd.read_csv("https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv?accessType=DOWNLOAD")
baby_names["Child's First Name"].tolist()
baby_names["Child's First Name"].to_dict()

"!".join(["a", "b", "c"])
", ".join(baby_names["Child's First Name"].str.title().drop_duplicates().sort_values())

# Export csv
baby_names.to_csv("NYC_Baby_Names.csv", index=False, columns=["Gender", "Ethnicity", "Child's First Name"],
                  encoding="utf-8")

# Import Excel
pd.read_excel("Data - Single Worksheet.xlsx")
pd.read_excel("Data - Multiple Worksheets.xlsx", sheet_name="Data 2")
data = pd.read_excel("Data - Multiple Worksheets.xlsx", sheet_name=[0, 1])  # dictionary of sheet #/names and data.frame
data = pd.read_excel("Data - Multiple Worksheets.xlsx", sheet_name=["Data 1", "Data 2"])
data = pd.read_excel("Data - Multiple Worksheets.xlsx", sheet_name=None)  # all worksheets

# Export Excel
girls = baby_names[baby_names.Gender == "FEMALE"]
boys = baby_names[baby_names.Gender == "MALE"]
excel_file = pd.ExcelWriter("Baby_Names.xlsx")
girls.to_excel(excel_file, sheet_name="Girls", index=False)
boys.to_excel(excel_file, sheet_name="Boys", index=False, columns=["Year of Birth", "Gender", "Ethnicity"])
excel_file.save()  # haven't saved until now
