import pandas as pd
import numpy as np

data = np.random.randint(0, 100, [1000, 50])
df = pd.DataFrame(data)
pd.options.display.max_rows = 2
pd.options.display.max_columns = 3
df

pd.get_option("max_rows")
pd.set_option("max_rows", 16)
pd.describe_option("max_rows")

# Precision
df = pd.DataFrame(np.random.randn(5, 5))
df
pd.get_option("precision")
pd.set_option("precision", 2)
df
pd.reset_option("precision")
