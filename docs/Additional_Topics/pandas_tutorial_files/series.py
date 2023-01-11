import pandas as pd

# Series: 1-d array
ice_cream = ["Chocolate", "Vanilla", "Strawberry", "Rum Raisin"]
pd.Series(ice_cream)

lottery = [1,2,3,4,5]
pd.Series(lottery)

webster = {"Aardvark" : "An animal",
           "Banana" : "A delicious fruit",
           "Cyan" : "A color"}
pd.Series(webster)

about_me = ["Smart", "Handsome", "Charming", "Brilliant", "Humble"]
s = pd.Series(about_me)
s.values
s.index

prices = [2.99, 4.45, 1.36]
s = pd.Series(prices)
s.sum()

pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze=True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)
type(pokemon)
dir(pokemon)
sorted(pokemon)
list(pokemon)
google.max()
max(google)

pokemon.sort_values().head()
google = google.sort_values(ascending = False, inplace = True)

"Bulbasaur" in pokemon # False
"Bulbasaur" in pokemon.values # True

pokemon[1]
pokemon[ [1, 2, 3] ]
pokemon[1:4]

pokemon = pd.read_csv("pokemon.csv", index_col = ["Pokemon"], squeeze=True)
pokemon[0]
pokemon["Bulbasaur"]
pokemon["Charmander":"Weedle"] # Upper included
pokemon[["Pikachu", "Digimon"]] # Error, no digimon
pokemon.reindex(index = ["Pikachu", "Digimon"])

pokemon.sort_index(inplace = True)
pokemon.get(0)

google = pd.read_csv("google_stock_price.csv", squeeze = True)
google.count() # exclude null values
len(google) # counts null values
google.describe()
google.max()
google.idxmax()

pokemon = pd.read_csv("pokemon.csv", index_col = ["Pokemon"], squeeze=True)
pokemon.value_counts()

def classify_performance(number):
    if number < 300:
        return "OK"
    elif number >= 300 and number < 650:
        return "Satisfactory"
    else:
        return "Incredible!"
google.apply(classify_performance)
google.apply(lambda stock_price : stock_price + 1)

pokemon_names = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze=True)
pokemon_types = pd.read_csv("pokemon.csv", index_col = "Pokemon", squeeze=True)
pokemon_names.map(pokemon_types)

pokemon_names = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze=True)
pokemon_types = pd.read_csv("pokemon.csv", index_col = "Pokemon", squeeze=True).to_dict()
pokemon_names.map(pokemon_types)