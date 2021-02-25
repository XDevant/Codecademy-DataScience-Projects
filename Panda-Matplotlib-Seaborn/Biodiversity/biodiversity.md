# Capstone 2: Biodiversity Project

# Introduction
You are a biodiversity analyst working for the National Parks Service.  You're going to help them analyze some data about species at various national parks.

Note: The data that you'll be working with for this project is *inspired* by real data, but is mostly fictional.

# Step 1
Import the modules that you'll be using in this assignment:
- `from matplotlib import pyplot as plt`
- `import pandas as pd`


```python
from matplotlib import pyplot as plt
import pandas as pd

```

# Step 2
You have been given two CSV files. `species_info.csv` with data about different species in our National Parks, including:
- The scientific name of each species
- The common names of each species
- The species conservation status

Load the dataset and inspect it:
- Load `species_info.csv` into a DataFrame called `species`


```python
species = pd.read_csv('species_info.csv')
```

Inspect each DataFrame using `.head()`.


```python
species.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>scientific_name</th>
      <th>common_names</th>
      <th>conservation_status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mammal</td>
      <td>Clethrionomys gapperi gapperi</td>
      <td>Gapper's Red-Backed Vole</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mammal</td>
      <td>Bos bison</td>
      <td>American Bison, Bison</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mammal</td>
      <td>Bos taurus</td>
      <td>Aurochs, Aurochs, Domestic Cattle (Feral), Dom...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mammal</td>
      <td>Ovis aries</td>
      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mammal</td>
      <td>Cervus elaphus</td>
      <td>Wapiti Or Elk</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# Step 3
Let's start by learning a bit more about our data.  Answer each of the following questions.

How many different species are in the `species` DataFrame?


```python
print(len(species))
```

    5824
    

What are the different values of `category` in `species`?


```python
print(species.category.unique())
```

    ['Mammal' 'Bird' 'Reptile' 'Amphibian' 'Fish' 'Vascular Plant'
     'Nonvascular Plant']
    

What are the different values of `conservation_status`?


```python
print(species.conservation_status.unique())
```

    [nan 'Species of Concern' 'Endangered' 'Threatened' 'In Recovery']
    

# Step 4
Let's start doing some analysis!

The column `conservation_status` has several possible values:
- `Species of Concern`: declining or appear to be in need of conservation
- `Threatened`: vulnerable to endangerment in the near future
- `Endangered`: seriously at risk of extinction
- `In Recovery`: formerly `Endangered`, but currnetly neither in danger of extinction throughout all or a significant portion of its range

We'd like to count up how many species meet each of these criteria.  Use `groupby` to count how many `scientific_name` meet each of these criteria.


```python
df = species.groupby('conservation_status').scientific_name.count().reset_index()
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>conservation_status</th>
      <th>scientific_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Endangered</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>In Recovery</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Species of Concern</td>
      <td>161</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Threatened</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



As we saw before, there are far more than 200 species in the `species` table.  Clearly, only a small number of them are categorized as needing some sort of protection.  The rest have `conservation_status` equal to `None`.  Because `groupby` does not include `None`, we will need to fill in the null values.  We can do this using `.fillna`.  We pass in however we want to fill in our `None` values as an argument.

Paste the following code and run it to see replace `None` with `No Intervention`:
```python
species.fillna('No Intervention', inplace=True)
```


```python
species.fillna('No Intervention', inplace=True)
```

Great! Now run the same `groupby` as before to see how many species require `No Intervention`.


```python
df = species.groupby('conservation_status').scientific_name.count().reset_index()
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>conservation_status</th>
      <th>scientific_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Endangered</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>In Recovery</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>No Intervention</td>
      <td>5633</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Species of Concern</td>
      <td>161</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Threatened</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



Let's use `plt.bar` to create a bar chart.  First, let's sort the columns by how many species are in each categories.  We can do this using `.sort_values`.  We use the the keyword `by` to indicate which column we want to sort by.

Paste the following code and run it to create a new DataFrame called `protection_counts`, which is sorted by `scientific_name`:
```python
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')
```


```python
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')
```

Now let's create a bar chart!
1. Start by creating a wide figure with `figsize=(10, 4)`
1. Start by creating an axes object called `ax` using `plt.subplot`.
2. Create a bar chart whose heights are equal to `scientific_name` column of `protection_counts`.
3. Create an x-tick for each of the bars.
4. Label each x-tick with the label from `conservation_status` in `protection_counts`
5. Label the y-axis `Number of Species`
6. Title the graph `Conservation Status by Species`
7. Plot the grap using `plt.show()`


```python
plt.figure(figsize = (10, 8))
ax = plt.subplot()
plt.bar(range(len(protection_counts)), protection_counts.scientific_name)

ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status)
plt.title('Conservation Status by Species')
plt.xlabel('Status')
plt.ylabel('Number of Species')

plt.show()
```


![png](output_24_0.png)


# Step 4
Are certain types of species more likely to be endangered?

Let's create a new column in `species` called `is_protected`, which is `True` if `conservation_status` is not equal to `No Intervention`, and `False` otherwise.


```python
species['is_protected'] =\
    species.apply(lambda row: True if row.conservation_status != 'No Intervention' else False  , axis = 1)
```

Let's group the `species` data frame by the `category` and `is_protected` columns and count the unique `scientific_name`s in each grouping.

Save your results to `category_counts`.


```python
category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()
```

Examine `category_counts` using `head()`.


```python
category_counts.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>is_protected</th>
      <th>scientific_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Amphibian</td>
      <td>False</td>
      <td>72</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Amphibian</td>
      <td>True</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bird</td>
      <td>False</td>
      <td>413</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bird</td>
      <td>True</td>
      <td>75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Fish</td>
      <td>False</td>
      <td>115</td>
    </tr>
  </tbody>
</table>
</div>



It's going to be easier to view this data if we pivot it.  Using `pivot`, rearange `category_counts` so that:
- `columns` is `is_protected`
- `index` is `category`
- `values` is `scientific_name`

Save your pivoted data to `category_pivot`. Remember to `reset_index()` at the end.


```python
category_pivot = category_counts.pivot(columns='is_protected',
                                       index='category', values='scientific_name').reset_index()
```

Examine `category_pivot`.


```python
category_pivot.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>is_protected</th>
      <th>category</th>
      <th>False</th>
      <th>True</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Amphibian</td>
      <td>72</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bird</td>
      <td>413</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fish</td>
      <td>115</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mammal</td>
      <td>146</td>
      <td>30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nonvascular Plant</td>
      <td>328</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



Use the `.columns` property to  rename the categories `True` and `False` to something more description:
- Leave `category` as `category`
- Rename `False` to `not_protected`
- Rename `True` to `protected`


```python
category_pivot.columns = ['category', 'not_protected', 'protected']
```

Let's create a new column of `category_pivot` called `percent_protected`, which is equal to `protected` (the number of species that are protected) divided by `protected` plus `not_protected` (the total number of species).


```python
category_pivot['percent_protected'] =\
    category_pivot.apply(lambda row: row.protected/(row.protected+row.not_protected), axis=1)
```

Examine `category_pivot`.


```python
category_pivot
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>not_protected</th>
      <th>protected</th>
      <th>percent_protected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Amphibian</td>
      <td>72</td>
      <td>7</td>
      <td>0.088608</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bird</td>
      <td>413</td>
      <td>75</td>
      <td>0.153689</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fish</td>
      <td>115</td>
      <td>11</td>
      <td>0.087302</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mammal</td>
      <td>146</td>
      <td>30</td>
      <td>0.170455</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nonvascular Plant</td>
      <td>328</td>
      <td>5</td>
      <td>0.015015</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Reptile</td>
      <td>73</td>
      <td>5</td>
      <td>0.064103</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Vascular Plant</td>
      <td>4216</td>
      <td>46</td>
      <td>0.010793</td>
    </tr>
  </tbody>
</table>
</div>



It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`.  We're going to do a significance test to see if this statement is true.  Before you do the significance test, consider the following questions:
- Is the data numerical or categorical?
- How many pieces of data are you comparing?

Based on those answers, you should choose to do a *chi squared test*.  In order to run a chi squared test, we'll need to create a contingency table.  Our contingency table should look like this:

||protected|not protected|
|-|-|-|
|Mammal|?|?|
|Bird|?|?|

Create a table called `contingency` and fill it in with the correct numbers


```python
contingency = [[30, 146], [75, 413]]
```

In order to perform our chi square test, we'll need to import the correct function from scipy.  Past the following code and run it:
```py
from scipy.stats import chi2_contingency
```


```python
from scipy.stats import chi2_contingency
```

Now run `chi2_contingency` with `contingency`.


```python
chi = chi2_contingency(contingency)
print(chi)
```

    (0.1617014831654557, 0.6875948096661336, 1, array([[ 27.8313253, 148.1686747],
           [ 77.1686747, 410.8313253]]))
    

It looks like this difference isn't significant!

Let's test another.  Is the difference between `Reptile` and `Mammal` significant?


```python
contingency2 = [[30, 146], [5, 73]]
chi2 = chi2_contingency(contingency2)
print(chi2)
```

    (4.289183096203645, 0.03835559022969898, 1, array([[ 24.2519685, 151.7480315],
           [ 10.7480315,  67.2519685]]))
    

Yes! It looks like there is a significant difference between `Reptile` and `Mammal`!

# Step 5

Conservationists have been recording sightings of different species at several national parks for the past 7 days.  They've saved sent you their observations in a file called `observations.csv`.  Load `observations.csv` into a variable called `observations`, then use `head` to view the data.


```python
observations = pd.read_csv('observations.csv')
observations.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>scientific_name</th>
      <th>park_name</th>
      <th>observations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Vicia benghalensis</td>
      <td>Great Smoky Mountains National Park</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Neovison vison</td>
      <td>Great Smoky Mountains National Park</td>
      <td>77</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Prunus subcordata</td>
      <td>Yosemite National Park</td>
      <td>138</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Abutilon theophrasti</td>
      <td>Bryce National Park</td>
      <td>84</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Githopsis specularioides</td>
      <td>Great Smoky Mountains National Park</td>
      <td>85</td>
    </tr>
  </tbody>
</table>
</div>



Some scientists are studying the number of sheep sightings at different national parks.  There are several different scientific names for different types of sheep.  We'd like to know which rows of `species` are referring to sheep.  Notice that the following code will tell us whether or not a word occurs in a string:


```python
# Does "Sheep" occur in this string?
str1 = 'This string contains Sheep'
'Sheep' in str1
```




    True




```python
# Does "Sheep" occur in this string?
str2 = 'This string contains Cows'
'Sheep' in str2
```




    False



Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise.


```python
species['is_sheep'] = species.apply(lambda row: 'Sheep' in row.common_names, axis=1)
species
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>scientific_name</th>
      <th>common_names</th>
      <th>conservation_status</th>
      <th>is_protected</th>
      <th>is_sheep</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mammal</td>
      <td>Clethrionomys gapperi gapperi</td>
      <td>Gapper's Red-Backed Vole</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mammal</td>
      <td>Bos bison</td>
      <td>American Bison, Bison</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mammal</td>
      <td>Bos taurus</td>
      <td>Aurochs, Aurochs, Domestic Cattle (Feral), Dom...</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mammal</td>
      <td>Ovis aries</td>
      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mammal</td>
      <td>Cervus elaphus</td>
      <td>Wapiti Or Elk</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5819</th>
      <td>Vascular Plant</td>
      <td>Solanum parishii</td>
      <td>Parish's Nightshade</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5820</th>
      <td>Vascular Plant</td>
      <td>Solanum xanti</td>
      <td>Chaparral Nightshade, Purple Nightshade</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5821</th>
      <td>Vascular Plant</td>
      <td>Parthenocissus vitacea</td>
      <td>Thicket Creeper, Virginia Creeper, Woodbine</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5822</th>
      <td>Vascular Plant</td>
      <td>Vitis californica</td>
      <td>California Grape, California Wild Grape</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5823</th>
      <td>Vascular Plant</td>
      <td>Tribulus terrestris</td>
      <td>Bullhead, Caltrop, Goathead, Mexican Sandbur, ...</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>5824 rows × 6 columns</p>
</div>



Select the rows of `species` where `is_sheep` is `True` and examine the results.


```python
df = species[(species.is_sheep == True)]
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>scientific_name</th>
      <th>common_names</th>
      <th>conservation_status</th>
      <th>is_protected</th>
      <th>is_sheep</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Mammal</td>
      <td>Ovis aries</td>
      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1139</th>
      <td>Vascular Plant</td>
      <td>Rumex acetosella</td>
      <td>Sheep Sorrel, Sheep Sorrell</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2233</th>
      <td>Vascular Plant</td>
      <td>Festuca filiformis</td>
      <td>Fineleaf Sheep Fescue</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3014</th>
      <td>Mammal</td>
      <td>Ovis canadensis</td>
      <td>Bighorn Sheep, Bighorn Sheep</td>
      <td>Species of Concern</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3758</th>
      <td>Vascular Plant</td>
      <td>Rumex acetosella</td>
      <td>Common Sheep Sorrel, Field Sorrel, Red Sorrel,...</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`.  Save the results to the variable `sheep_species`.


```python
sheep_species = species[(species.is_sheep == True)&(species.category == 'Mammal')]
sheep_species
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>scientific_name</th>
      <th>common_names</th>
      <th>conservation_status</th>
      <th>is_protected</th>
      <th>is_sheep</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Mammal</td>
      <td>Ovis aries</td>
      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>
      <td>No Intervention</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3014</th>
      <td>Mammal</td>
      <td>Ovis canadensis</td>
      <td>Bighorn Sheep, Bighorn Sheep</td>
      <td>Species of Concern</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4446</th>
      <td>Mammal</td>
      <td>Ovis canadensis sierrae</td>
      <td>Sierra Nevada Bighorn Sheep</td>
      <td>Endangered</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`.


```python
sheep_observations = pd.merge(sheep_species, observations)
```

How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.

This is the total number of sheep observed in each park over the past 7 days.


```python
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
obs_by_park
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>park_name</th>
      <th>observations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bryce National Park</td>
      <td>250</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Great Smoky Mountains National Park</td>
      <td>149</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Yellowstone National Park</td>
      <td>507</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Yosemite National Park</td>
      <td>282</td>
    </tr>
  </tbody>
</table>
</div>



Create a bar chart showing the different number of observations per week at each park.

1. Start by creating a wide figure with `figsize=(16, 4)`
1. Start by creating an axes object called `ax` using `plt.subplot`.
2. Create a bar chart whose heights are equal to `observations` column of `obs_by_park`.
3. Create an x-tick for each of the bars.
4. Label each x-tick with the label from `park_name` in `obs_by_park`
5. Label the y-axis `Number of Observations`
6. Title the graph `Observations of Sheep per Week`
7. Plot the grap using `plt.show()`


```python
plt.figure(figsize = (16, 4))
ax1 = plt.subplot()
plt.bar(range(len(obs_by_park)), obs_by_park.observations)

ax1.set_xticks(range(len(obs_by_park)))
ax1.set_xticklabels(obs_by_park.park_name)
plt.title('Observations of Sheep per Week')
plt.xlabel('National Park')
plt.ylabel('Number of Observations')

plt.show()
```


![png](output_69_0.png)


Our scientists know that 15% of sheep at Bryce National Park have foot and mouth disease.  Park rangers at Yellowstone National Park have been running a program to reduce the rate of foot and mouth disease at that park.  The scientists want to test whether or not this program is working.  They want to be able to detect reductions of at least 5 percentage points.  For instance, if 10% of sheep in Yellowstone have foot and mouth disease, they'd like to be able to know this, with confidence.

Use <a href="https://s3.amazonaws.com/codecademy-content/courses/learn-hypothesis-testing/a_b_sample_size/index.html">Codecademy's sample size calculator</a> to calculate the number of sheep that they would need to observe from each park.  Use the default level of significance (90%).

Remember that "Minimum Detectable Effect" is a percent of the baseline.


```python
number of sheep = 890 (baseline = 15%, Minimum Detectable Effect = 33%)
```

How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?


```python
At Bryce National Park: 4 weeks, at Yellowstone National Park: 2 weeks
```
