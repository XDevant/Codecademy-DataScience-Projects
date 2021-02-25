# Project: Visualizing Race and Gender Representation In American Movies
# 
# **The Bechdel-Wallace Test** — often abbreviated to the "Bechdel Test" — evaluates movies based on two simple questions:
# 
#   1.  Does the movie have at least two named female characters?
#   2.  And do those characters have at least one conversation that is not about a man?

# 1. SETUP

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('bechdelExpanded.csv')

print(df.head())

print(df.info())

df['total_score'] = df.apply(lambda row: row.bechdel + row.waithe + row.ko , axis=1)

print(df.head())

# 4. Sorting Data

df_sorted = df.sort_values("total_score").reset_index(drop = True)
print(df_sorted.head())

# ## 5. Isolating the Data
df_partial = df_sorted[['movie', 'bechdel', 'waithe', 'ko', 'total_score']]

print(df_partial.head())

# 6. Plot DataFrame with Matplotlib

ax = df_partial[['movie','total_score']].set_index('movie')

ax.plot(kind = 'bar',
       title ='Representation In Movies',
       figsize=(15, 10),
       legend=True)

# 7. Iterate and Discover Meaning

ax.plot(kind = 'barh',
       title ='Representation In Movies',
       figsize=(15, 10),
       legend=True, fontsize=12)

