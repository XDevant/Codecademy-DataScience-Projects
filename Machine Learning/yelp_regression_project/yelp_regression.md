# Project: Yelp Rating Regression Predictor

The restaurant industry is tougher than ever, with restaurant reviews blazing across the Internet from day one of a restaurant's opening. But as a lover of food, you and your friend decide to break into the industry and open up your own restaurant, Danielle's Delicious Delicacies. Since a restaurant's success is highly correlated with its reputation, you want to make sure Danielle's Delicious Delicacies has the best reviews on the most queried restaurant review site: Yelp! While you know your food will be delicious, you think there are other factors that play into a Yelp rating and will ultimately determine your business's success. With a dataset of different restaurant features and their Yelp ratings, you decide to use a Multiple Linear Regression model to investigate what factors most affect a restaurant's Yelp rating and predict the Yelp rating for your restaurant!

In this project we'll be working with a real dataset provided by Yelp. We have provided six files, listed below with a brief description:
* `yelp_business.json`: establishment data regarding location and attributes for all businesses in the dataset
* `yelp_review.json`: Yelp review metadata by business
* `yelp_user.json`: user profile metadata by business
* `yelp_checkin.json`: online checkin metadata by business
* `yelp_tip.json`: tip metadata by business
* `yelp_photo.json`: photo metadata by business

For a more detailed explanation of the features in each `.json` file, see the accompanying [explanatory feature document](https://docs.google.com/document/d/1V6FjJpKspVBOOBs4E7fBfp_yzHn0--XJkC2uUtWuRgM/edit).

Let's get started by exploring the data in each of these files to see what we are working with.

## Load the Data and Take a Peek

To get a better understanding of the dataset we can use Pandas to explore the data in DataFrame form. In the code block below we have imported Pandas for you. The `read_json()` method reads data from a json file into a DataFrame, as shown below:
```python
df = pd.read_json('file_name.json', lines=True)
```
Load the data from each of the json files with the following naming conventions:
* `yelp_business.json` into a DataFrame named `businesses`
* `yelp_review.json` into a DataFrame named `reviews`
* `yelp_user.json` into a DataFrame named `users`
* `yelp_checkin.json` into a DataFrame named `checkins`
* `yelp_tip.json` into a DataFrame named `tips`
* `yelp_photo.json` into a DataFrame named `photos`

Importing that data could take 10 to 20 seconds to run depending on your computer, but don't worry, once it's loaded in you're ready to go!


```python
import pandas as pd

businesses = pd.read_json('yelp_business.json', lines=True)
reviews = pd.read_json('yelp_review.json', lines=True)
users = pd.read_json('yelp_user.json', lines=True)
checkins = pd.read_json('yelp_checkin.json', lines=True)
tips = pd.read_json('yelp_tip.json', lines=True)
photos = pd.read_json('yelp_photo.json', lines=True)


```

In order to more clearly see the information in our DataFrame, we can adjust the number of columns shown (`max_columns`) and the number of characters shown in a column (`max_colwidth`) with the below code:

```python
pd.options.display.max_columns = number_of_columns_to_display
pd.options.display.max_colwidth = number_of_characters_to_display
```

Set `max_columns` to `60` and `max_colwidth` to `500`. We are working with some BIG data here!


```python
pd.options.display.max_columns = 60
pd.options.display.max_colwidth = 500
```

Inspect the first five rows of each DataFrame using the `.head()` method to get an overview of the data (make sure to check each DataFrame in a separate cell in order to view it properly).


```python
businesses.head()
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
      <th>address</th>
      <th>alcohol?</th>
      <th>attributes</th>
      <th>business_id</th>
      <th>categories</th>
      <th>city</th>
      <th>good_for_kids</th>
      <th>has_bike_parking</th>
      <th>has_wifi</th>
      <th>hours</th>
      <th>is_open</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>name</th>
      <th>neighborhood</th>
      <th>postal_code</th>
      <th>price_range</th>
      <th>review_count</th>
      <th>stars</th>
      <th>state</th>
      <th>take_reservations</th>
      <th>takes_credit_cards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1314 44 Avenue NE</td>
      <td>0</td>
      <td>{'BikeParking': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': '{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}', 'GoodForKids': 'True', 'HasTV': 'True', 'NoiseLevel': 'average', 'OutdoorSeating': 'False', 'RestaurantsAttire': 'casual', 'RestaurantsDelivery': 'False', 'RestaurantsGoodForGroups': 'True', 'RestaurantsPriceRange2': '2', 'RestaurantsReservations': 'True', 'RestaurantsTakeOut': 'True'}</td>
      <td>Apn5Q_b6Nz61Tq4XzPdf9A</td>
      <td>Tours, Breweries, Pizza, Restaurants, Food, Hotels &amp; Travel</td>
      <td>Calgary</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>{'Monday': '8:30-17:0', 'Tuesday': '11:0-21:0', 'Wednesday': '11:0-21:0', 'Thursday': '11:0-21:0', 'Friday': '11:0-21:0', 'Saturday': '11:0-21:0'}</td>
      <td>1</td>
      <td>51.091813</td>
      <td>-114.031675</td>
      <td>Minhas Micro Brewery</td>
      <td></td>
      <td>T2E 6L6</td>
      <td>2</td>
      <td>24</td>
      <td>4.0</td>
      <td>AB</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td>0</td>
      <td>{'Alcohol': 'none', 'BikeParking': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': '{'garage': False, 'street': True, 'validated': False, 'lot': True, 'valet': False}', 'Caters': 'True', 'DogsAllowed': 'True', 'DriveThru': 'False', 'GoodForKids': 'True', 'GoodForMeal': '{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'breakfast': False, 'brunch': False}', 'HasTV': 'False', 'OutdoorSeating': 'True', 'RestaurantsAttire': 'casual', 'RestaurantsDelivery'...</td>
      <td>AjEbIBw6ZFfln7ePHha9PA</td>
      <td>Chicken Wings, Burgers, Caterers, Street Vendors, Barbeque, Food Trucks, Food, Restaurants, Event Planning &amp; Services</td>
      <td>Henderson</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>{'Friday': '17:0-23:0', 'Saturday': '17:0-23:0', 'Sunday': '17:0-23:0'}</td>
      <td>0</td>
      <td>35.960734</td>
      <td>-114.939821</td>
      <td>CK'S BBQ &amp; Catering</td>
      <td></td>
      <td>89002</td>
      <td>2</td>
      <td>3</td>
      <td>4.5</td>
      <td>NV</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1335 rue Beaubien E</td>
      <td>1</td>
      <td>{'Alcohol': 'beer_and_wine', 'Ambience': '{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': False}', 'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'False', 'BusinessParking': '{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}', 'Caters': 'False', 'GoodForKids': 'True', 'GoodForMeal': '{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'breakfa...</td>
      <td>O8S5hYJ1SMc8fA4QBtVujA</td>
      <td>Breakfast &amp; Brunch, Restaurants, French, Sandwiches, Cafes</td>
      <td>Montréal</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>{'Monday': '10:0-22:0', 'Tuesday': '10:0-22:0', 'Wednesday': '10:0-22:0', 'Thursday': '10:0-22:0', 'Friday': '10:0-22:0', 'Saturday': '10:0-22:0', 'Sunday': '10:0-22:0'}</td>
      <td>0</td>
      <td>45.540503</td>
      <td>-73.599300</td>
      <td>La Bastringue</td>
      <td>Rosemont-La Petite-Patrie</td>
      <td>H2G 1K7</td>
      <td>2</td>
      <td>5</td>
      <td>4.0</td>
      <td>QC</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>211 W Monroe St</td>
      <td>0</td>
      <td>None</td>
      <td>bFzdJJ3wp3PZssNEsyU23g</td>
      <td>Insurance, Financial Services</td>
      <td>Phoenix</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>None</td>
      <td>1</td>
      <td>33.449999</td>
      <td>-112.076979</td>
      <td>Geico Insurance</td>
      <td></td>
      <td>85003</td>
      <td>0</td>
      <td>8</td>
      <td>1.5</td>
      <td>AZ</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005 Alyth Place SE</td>
      <td>0</td>
      <td>{'BusinessAcceptsCreditCards': 'True'}</td>
      <td>8USyCYqpScwiNEb58Bt6CA</td>
      <td>Home &amp; Garden, Nurseries &amp; Gardening, Shopping, Local Services, Automotive, Electronics Repair</td>
      <td>Calgary</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>{'Monday': '8:0-17:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}</td>
      <td>1</td>
      <td>51.035591</td>
      <td>-114.027366</td>
      <td>Action Engine</td>
      <td></td>
      <td>T2H 0N5</td>
      <td>0</td>
      <td>4</td>
      <td>2.0</td>
      <td>AB</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
reviews.head()
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
      <th>business_id</th>
      <th>average_review_age</th>
      <th>average_review_length</th>
      <th>average_review_sentiment</th>
      <th>number_funny_votes</th>
      <th>number_cool_votes</th>
      <th>number_useful_votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>--1UhMGODdWsrMastO9DZw</td>
      <td>524.458333</td>
      <td>466.208333</td>
      <td>0.808638</td>
      <td>1</td>
      <td>16</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>--6MefnULPED_I942VcFNA</td>
      <td>1199.589744</td>
      <td>785.205128</td>
      <td>0.669126</td>
      <td>27</td>
      <td>32</td>
      <td>53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>--7zmmkVg-IMGaXbuVd0SQ</td>
      <td>717.851852</td>
      <td>536.592593</td>
      <td>0.820837</td>
      <td>29</td>
      <td>52</td>
      <td>81</td>
    </tr>
    <tr>
      <th>3</th>
      <td>--8LPVSo5i0Oo61X01sV9A</td>
      <td>751.750000</td>
      <td>478.250000</td>
      <td>0.170925</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>--9QQLMTbFzLJ_oT-ON3Xw</td>
      <td>978.727273</td>
      <td>436.181818</td>
      <td>0.562264</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
users.head()
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
      <th>business_id</th>
      <th>average_number_friends</th>
      <th>average_days_on_yelp</th>
      <th>average_number_fans</th>
      <th>average_review_count</th>
      <th>average_number_years_elite</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>--1UhMGODdWsrMastO9DZw</td>
      <td>18.791667</td>
      <td>1789.750000</td>
      <td>1.833333</td>
      <td>57.541667</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>--6MefnULPED_I942VcFNA</td>
      <td>214.564103</td>
      <td>2039.948718</td>
      <td>49.256410</td>
      <td>332.743590</td>
      <td>1.769231</td>
    </tr>
    <tr>
      <th>2</th>
      <td>--7zmmkVg-IMGaXbuVd0SQ</td>
      <td>126.185185</td>
      <td>1992.796296</td>
      <td>19.222222</td>
      <td>208.962963</td>
      <td>1.814815</td>
    </tr>
    <tr>
      <th>3</th>
      <td>--8LPVSo5i0Oo61X01sV9A</td>
      <td>25.250000</td>
      <td>2095.750000</td>
      <td>0.500000</td>
      <td>7.500000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>--9QQLMTbFzLJ_oT-ON3Xw</td>
      <td>52.454545</td>
      <td>1804.636364</td>
      <td>1.000000</td>
      <td>34.636364</td>
      <td>0.090909</td>
    </tr>
  </tbody>
</table>
</div>




```python
checkins.head()
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
      <th>business_id</th>
      <th>time</th>
      <th>weekday_checkins</th>
      <th>weekend_checkins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7KPBkxAOEtb3QeIL9PEErg</td>
      <td>{'Fri-0': 2, 'Sat-0': 1, 'Sun-0': 1, 'Wed-0': 2, 'Fri-1': 1, 'Sat-1': 3, 'Thu-1': 1, 'Wed-1': 1, 'Sat-2': 1, 'Sun-2': 2, 'Thu-2': 1, 'Wed-2': 1, 'Fri-3': 1, 'Sun-3': 3, 'Mon-4': 1, 'Thu-4': 1, 'Tue-4': 2, 'Wed-4': 2, 'Sun-6': 1, 'Wed-6': 1, 'Thu-7': 1, 'Fri-10': 3, 'Mon-10': 1, 'Sat-10': 3, 'Sun-10': 3, 'Tue-10': 2, 'Mon-11': 1, 'Thu-11': 1, 'Wed-11': 2, 'Mon-12': 1, 'Sat-12': 1, 'Tue-12': 1, 'Sat-13': 3, 'Thu-13': 1, 'Tue-13': 2, 'Wed-13': 3, 'Fri-14': 2, 'Mon-14': 1, 'Sat-14': 1, 'Sun-14':...</td>
      <td>76</td>
      <td>75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kREVIrSBbtqBhIYkTccQUg</td>
      <td>{'Mon-13': 1, 'Thu-13': 1, 'Sat-16': 1, 'Wed-17': 1, 'Sun-19': 1, 'Thu-20': 1, 'Sat-21': 1}</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tJRDll5yqpZwehenzE2cSg</td>
      <td>{'Thu-0': 1, 'Mon-1': 1, 'Mon-12': 1, 'Sat-16': 1, 'Sun-22': 1, 'Fri-23': 1}</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tZccfdl6JNw-j5BKnCTIQQ</td>
      <td>{'Sun-14': 1, 'Fri-18': 1, 'Mon-20': 1}</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>r1p7RAMzCV_6NPF0dNoR3g</td>
      <td>{'Sat-3': 1, 'Sun-18': 1, 'Sat-21': 1, 'Sat-23': 1, 'Thu-23': 1}</td>
      <td>1</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.head()
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
      <th>business_id</th>
      <th>average_tip_length</th>
      <th>number_tips</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>--1UhMGODdWsrMastO9DZw</td>
      <td>79.000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>--6MefnULPED_I942VcFNA</td>
      <td>49.857143</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>--7zmmkVg-IMGaXbuVd0SQ</td>
      <td>52.500000</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>--9QQLMTbFzLJ_oT-ON3Xw</td>
      <td>136.500000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>--9e1ONYQuAa-CB_Rrw7Tw</td>
      <td>68.064935</td>
      <td>154</td>
    </tr>
  </tbody>
</table>
</div>




```python
photos.head()
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
      <th>business_id</th>
      <th>average_caption_length</th>
      <th>number_pics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>--1UhMGODdWsrMastO9DZw</td>
      <td>0.000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>--6MefnULPED_I942VcFNA</td>
      <td>67.500000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>--9e1ONYQuAa-CB_Rrw7Tw</td>
      <td>30.426471</td>
      <td>136</td>
    </tr>
    <tr>
      <th>3</th>
      <td>--DaPTJW3-tB1vP-PfdTEg</td>
      <td>0.000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>--FBCX-N37CMYDfs790Bnw</td>
      <td>5.500000</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



How many different businesses are in the dataset? What are the different features in the review DataFrame?


```python
print(reviews.columns)
print(businesses.business_id.count())
```

    Index(['business_id', 'average_review_age', 'average_review_length',
           'average_review_sentiment', 'number_funny_votes', 'number_cool_votes',
           'number_useful_votes'],
          dtype='object')
    188593
    

What is the range of values for the features in the user DataFrame?


```python
df = users.iloc[:,1:]
df.max()-df.min()
```




    average_number_friends        4218.000000
    average_days_on_yelp          4784.000000
    average_number_fans           1174.666667
    average_review_count          6334.333333
    average_number_years_elite      10.666667
    dtype: float64



What is the Yelp rating, or `stars`, of the establishment with `business_id` = `5EvUIR4IzCWUOm0PsUZXjA`. Use Pandas boolean indexing to find the Yelp rating, using the syntax below:

```python
df[df['column_we_know'] == 'value_we_know']['column_we_want']
```


```python
businesses[businesses['business_id'] == '5EvUIR4IzCWUOm0PsUZXjA']['stars']
```




    30781    3.0
    Name: stars, dtype: float64



 What feature, or column, do the DataFrames have in common?

## Merge the Data

Since we are working with data from several files, we need to combine the data into a single DataFrame that allows us to analyze the different features with respect to our target variable, the Yelp rating. We can do this by merging the multiple DataFrames we have together, joining them on the columns they have in common. In our case, this unique identifying column is the `business_id`. We can merge two DataFrames together with the following syntax:

```python
pd.merge(left, right, how='inner/outer/left/right', on='column(s)_to_merge_on')
```
* `left` is the DataFrame on the left side of our merge
* `right` is the DataFrame on the right side of our merge
* `how` describes the style of merge we want to complete (similar to inner/outer/left/right joins in SQL)
* `on` is the column or columns to perform the merge on (the column connecting the two tables)

Given our six DataFrames, we will need to perform 5 merges to combine all the data into one DataFrame. In the cell below we merged the business table and the review table into a new DataFrame, `df`, for you. After the merge we've added all the rows from `businesses` and `reviews` together, but kept the same total number of rows! Run the cell to perform the merge and confirm the number of rows in `df`. 


```python
df = pd.merge(businesses, reviews, how='left', on='business_id')
print(len(df))
```

    188593
    

Merge each of the other 4 DataFrames into our new DataFrame `df` to combine all the data together. Make sure that `df` is the left DataFrame in each merge and `how=left` since not every DataFrame includes every business in the dataset (this way we won't lose any data during the merges). Once combined, print out the columns of `df`. What features are in this new DataFrame?


```python
df = pd.merge(df, users, how='left', on='business_id')
df = pd.merge(df, checkins, how='left', on='business_id')
df = pd.merge(df, tips, how='left', on='business_id')
df = pd.merge(df, photos, how='left', on='business_id')
print(len(df))
print(df.columns)
```

    188593
    Index(['address', 'alcohol?', 'attributes', 'business_id', 'categories',
           'city', 'good_for_kids', 'has_bike_parking', 'has_wifi', 'hours',
           'is_open', 'latitude', 'longitude', 'name', 'neighborhood',
           'postal_code', 'price_range', 'review_count', 'stars', 'state',
           'take_reservations', 'takes_credit_cards', 'average_review_age',
           'average_review_length', 'average_review_sentiment',
           'number_funny_votes', 'number_cool_votes', 'number_useful_votes',
           'average_number_friends', 'average_days_on_yelp', 'average_number_fans',
           'average_review_count', 'average_number_years_elite', 'time',
           'weekday_checkins', 'weekend_checkins', 'average_tip_length',
           'number_tips', 'average_caption_length', 'number_pics'],
          dtype='object')
    

## Clean the Data

We are getting really close to the fun analysis part! We just have to clean our data a bit so we can focus on the features that might have predictive power for determining an establishment's Yelp rating.

In a Linear Regression model, our features will ideally be continuous variables that have an affect on our dependent variable, the Yelp rating. For this project with will also be working with some features that are binary, on the scale [0,1]. With this information, we can remove any columns in the dataset that are not continuous or binary, and that we do not want to make predictions on. The cell below contains a list of these unnecessary features. Drop them from `df` with Pandas' drop syntax, provided below:

```python
df.drop(list_of_features_to_remove, axis=1, inplace=True)
```

* `list_of_features_to_remove` is, you guessed it, the list of features we want to remove!
* `axis=1` lets Pandas know we want to drop columns, not rows, from our DataFrame (axis=0 is used for computations along rows!) 
* `inplace=True` lets us drop the columns right here in our DataFrame, instead of returning a new DataFrame that we could store in a new variable


```python
features_to_remove = ['address','attributes','business_id','categories','city','hours','is_open','latitude','longitude','name','neighborhood','postal_code','state','time']
df.drop(features_to_remove, axis=1, inplace=True)
print(df.columns)
```

    Index(['alcohol?', 'good_for_kids', 'has_bike_parking', 'has_wifi',
           'price_range', 'review_count', 'stars', 'take_reservations',
           'takes_credit_cards', 'average_review_age', 'average_review_length',
           'average_review_sentiment', 'number_funny_votes', 'number_cool_votes',
           'number_useful_votes', 'average_number_friends', 'average_days_on_yelp',
           'average_number_fans', 'average_review_count',
           'average_number_years_elite', 'weekday_checkins', 'weekend_checkins',
           'average_tip_length', 'number_tips', 'average_caption_length',
           'number_pics'],
          dtype='object')
    

Now we just have to check our data to make sure we don't have any missing values, or `NaN`s, which will prevent the Linear Regression model from running correctly. To do this we can use the statement `df.isna().any()`. This will check all of our columns and return `True` if there are any missing values or `NaN`s, or `False` if there are no missing values. Check if `df` is missing any values.


```python
df.isna().any()
```




    alcohol?                      False
    good_for_kids                 False
    has_bike_parking              False
    has_wifi                      False
    price_range                   False
    review_count                  False
    stars                         False
    take_reservations             False
    takes_credit_cards            False
    average_review_age            False
    average_review_length         False
    average_review_sentiment      False
    number_funny_votes            False
    number_cool_votes             False
    number_useful_votes           False
    average_number_friends        False
    average_days_on_yelp          False
    average_number_fans           False
    average_review_count          False
    average_number_years_elite    False
    weekday_checkins               True
    weekend_checkins               True
    average_tip_length             True
    number_tips                    True
    average_caption_length         True
    number_pics                    True
    dtype: bool



As you can see, there are a few columns with missing values. Since our dataset has no information recorded for some businesses in these columns, we will assume the Yelp pages did not display these features. For example, if there is a `NaN` value for `number_pics`, it means that the associated business did not have any pictures posted on its Yelp page. Thus we can replace all of our `NaN`s with `0`s. To do this we can use the `.fillna()` method, which takes a dictionary as shown below:

```python
df.fillna({'column_1':val_to_replace_na,
           'column_2':val_to_replace_na,
           'column_3':val_to_replace_na},
          inplace=True)
```

* `column_1`, `column_2`, and `column_3` are the columns with missing values that we want to fill. We can include as many columns as we like in the dictionary that is passed to `.fill_na()`
* `val_to_replace_na` is the value that will replace the missing values, or `NaN`s
* `inplace=True` since we want to perform our changes in place and not return a new DataFrame

Fill the missing values in `df` with `0`. Afterwards, confirm the missing values have been filled with `df.isna().any()`.


```python
df.fillna({'weekday_checkins':0,
           'weekend_checkins':0,
           'average_tip_length':0,
           'number_tips':0,
           'average_caption_length':0,
           'number_pics':0},
          inplace=True)
df.isna().any()
```




    alcohol?                      False
    good_for_kids                 False
    has_bike_parking              False
    has_wifi                      False
    price_range                   False
    review_count                  False
    stars                         False
    take_reservations             False
    takes_credit_cards            False
    average_review_age            False
    average_review_length         False
    average_review_sentiment      False
    number_funny_votes            False
    number_cool_votes             False
    number_useful_votes           False
    average_number_friends        False
    average_days_on_yelp          False
    average_number_fans           False
    average_review_count          False
    average_number_years_elite    False
    weekday_checkins              False
    weekend_checkins              False
    average_tip_length            False
    number_tips                   False
    average_caption_length        False
    number_pics                   False
    dtype: bool



## Exploratory Analysis

Now that our data is all together, let's investigate some of the different features to see what might correlate most with our dependent variable, the Yelp rating (called `stars` in our DataFrame). The features with the best correlations could prove to be the most helpful for our Linear Regression model! Pandas DataFrames have a really helpful method, `.corr()`, that allows us to see the correlation coefficients for each pair of our different features. Remember, a correlation of `0` indicates that two features have no linear relationship, a correlation coefficient of `1` indicates two features have a perfect positive linear relationship, and a correlation coefficient of `-1` indicates two features have a perfect negative linear relationship. Call `.corr()` on `df`. You'll see that `number_funny_votes` has a correlation coefficient of `0.001320` with respect to `stars`, our Yelp rating. This is a very weak correlation. What features best correlate, both positively and negatively, with Yelp rating?


```python
df.corr()
#[average_review_age, average_review_length, average_review_sentiment, has_bike_parking, has_bike_parking, average_number_years_elite, average_tip_length 
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
      <th>alcohol?</th>
      <th>good_for_kids</th>
      <th>has_bike_parking</th>
      <th>has_wifi</th>
      <th>price_range</th>
      <th>review_count</th>
      <th>stars</th>
      <th>take_reservations</th>
      <th>takes_credit_cards</th>
      <th>average_review_age</th>
      <th>average_review_length</th>
      <th>average_review_sentiment</th>
      <th>number_funny_votes</th>
      <th>number_cool_votes</th>
      <th>number_useful_votes</th>
      <th>average_number_friends</th>
      <th>average_days_on_yelp</th>
      <th>average_number_fans</th>
      <th>average_review_count</th>
      <th>average_number_years_elite</th>
      <th>weekday_checkins</th>
      <th>weekend_checkins</th>
      <th>average_tip_length</th>
      <th>number_tips</th>
      <th>average_caption_length</th>
      <th>number_pics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>alcohol?</th>
      <td>1.000000</td>
      <td>0.305284</td>
      <td>0.213318</td>
      <td>0.345032</td>
      <td>0.349004</td>
      <td>0.259836</td>
      <td>-0.043332</td>
      <td>0.601670</td>
      <td>0.190738</td>
      <td>0.139108</td>
      <td>0.037369</td>
      <td>0.097188</td>
      <td>0.117472</td>
      <td>0.188598</td>
      <td>0.165775</td>
      <td>0.015261</td>
      <td>0.129901</td>
      <td>0.017794</td>
      <td>0.026846</td>
      <td>0.099141</td>
      <td>0.094398</td>
      <td>0.131175</td>
      <td>0.098037</td>
      <td>0.208856</td>
      <td>0.305570</td>
      <td>0.252523</td>
    </tr>
    <tr>
      <th>good_for_kids</th>
      <td>0.305284</td>
      <td>1.000000</td>
      <td>0.271788</td>
      <td>0.258887</td>
      <td>0.205513</td>
      <td>0.162469</td>
      <td>-0.030382</td>
      <td>0.318729</td>
      <td>0.150360</td>
      <td>0.055847</td>
      <td>-0.079183</td>
      <td>0.073806</td>
      <td>0.060658</td>
      <td>0.113262</td>
      <td>0.083832</td>
      <td>0.016557</td>
      <td>0.045057</td>
      <td>0.024901</td>
      <td>0.040692</td>
      <td>0.094233</td>
      <td>0.068960</td>
      <td>0.079808</td>
      <td>0.121948</td>
      <td>0.156536</td>
      <td>0.291413</td>
      <td>0.175058</td>
    </tr>
    <tr>
      <th>has_bike_parking</th>
      <td>0.213318</td>
      <td>0.271788</td>
      <td>1.000000</td>
      <td>0.235138</td>
      <td>0.416044</td>
      <td>0.155505</td>
      <td>0.068084</td>
      <td>0.160129</td>
      <td>0.286298</td>
      <td>-0.080443</td>
      <td>-0.116295</td>
      <td>0.130448</td>
      <td>0.060595</td>
      <td>0.114094</td>
      <td>0.094000</td>
      <td>0.028307</td>
      <td>-0.045849</td>
      <td>0.018120</td>
      <td>0.031203</td>
      <td>0.083062</td>
      <td>0.082474</td>
      <td>0.093579</td>
      <td>0.144163</td>
      <td>0.147115</td>
      <td>0.180468</td>
      <td>0.109552</td>
    </tr>
    <tr>
      <th>has_wifi</th>
      <td>0.345032</td>
      <td>0.258887</td>
      <td>0.235138</td>
      <td>1.000000</td>
      <td>0.240796</td>
      <td>0.195737</td>
      <td>-0.039857</td>
      <td>0.312217</td>
      <td>0.155098</td>
      <td>-0.034258</td>
      <td>-0.037712</td>
      <td>0.054699</td>
      <td>0.082213</td>
      <td>0.147320</td>
      <td>0.120622</td>
      <td>0.015937</td>
      <td>0.000448</td>
      <td>0.023913</td>
      <td>0.044006</td>
      <td>0.082863</td>
      <td>0.107467</td>
      <td>0.126861</td>
      <td>0.104742</td>
      <td>0.173542</td>
      <td>0.258938</td>
      <td>0.210583</td>
    </tr>
    <tr>
      <th>price_range</th>
      <td>0.349004</td>
      <td>0.205513</td>
      <td>0.416044</td>
      <td>0.240796</td>
      <td>1.000000</td>
      <td>0.148277</td>
      <td>-0.052565</td>
      <td>0.316105</td>
      <td>0.400742</td>
      <td>0.189623</td>
      <td>0.003850</td>
      <td>0.089349</td>
      <td>0.073215</td>
      <td>0.119422</td>
      <td>0.098990</td>
      <td>0.087231</td>
      <td>0.176133</td>
      <td>0.104221</td>
      <td>0.122982</td>
      <td>0.210487</td>
      <td>0.057877</td>
      <td>0.081321</td>
      <td>0.129212</td>
      <td>0.119632</td>
      <td>0.170171</td>
      <td>0.143570</td>
    </tr>
    <tr>
      <th>review_count</th>
      <td>0.259836</td>
      <td>0.162469</td>
      <td>0.155505</td>
      <td>0.195737</td>
      <td>0.148277</td>
      <td>1.000000</td>
      <td>0.032413</td>
      <td>0.187755</td>
      <td>0.119984</td>
      <td>0.010070</td>
      <td>0.004748</td>
      <td>0.076265</td>
      <td>0.548164</td>
      <td>0.860767</td>
      <td>0.746949</td>
      <td>0.026206</td>
      <td>0.050451</td>
      <td>0.000474</td>
      <td>-0.002576</td>
      <td>0.014712</td>
      <td>0.567452</td>
      <td>0.699631</td>
      <td>0.094133</td>
      <td>0.844978</td>
      <td>0.224983</td>
      <td>0.610889</td>
    </tr>
    <tr>
      <th>stars</th>
      <td>-0.043332</td>
      <td>-0.030382</td>
      <td>0.068084</td>
      <td>-0.039857</td>
      <td>-0.052565</td>
      <td>0.032413</td>
      <td>1.000000</td>
      <td>-0.024486</td>
      <td>0.037748</td>
      <td>-0.125645</td>
      <td>-0.277081</td>
      <td>0.782187</td>
      <td>0.001320</td>
      <td>0.043375</td>
      <td>-0.000066</td>
      <td>-0.007629</td>
      <td>-0.038061</td>
      <td>-0.031141</td>
      <td>-0.066572</td>
      <td>-0.064419</td>
      <td>0.004130</td>
      <td>0.007863</td>
      <td>-0.052899</td>
      <td>0.014038</td>
      <td>0.000040</td>
      <td>0.001727</td>
    </tr>
    <tr>
      <th>take_reservations</th>
      <td>0.601670</td>
      <td>0.318729</td>
      <td>0.160129</td>
      <td>0.312217</td>
      <td>0.316105</td>
      <td>0.187755</td>
      <td>-0.024486</td>
      <td>1.000000</td>
      <td>0.127941</td>
      <td>0.064098</td>
      <td>0.046331</td>
      <td>0.086728</td>
      <td>0.071131</td>
      <td>0.129165</td>
      <td>0.115583</td>
      <td>-0.025522</td>
      <td>0.048850</td>
      <td>0.001131</td>
      <td>0.010618</td>
      <td>0.063990</td>
      <td>0.053162</td>
      <td>0.076183</td>
      <td>0.084098</td>
      <td>0.134832</td>
      <td>0.282823</td>
      <td>0.231242</td>
    </tr>
    <tr>
      <th>takes_credit_cards</th>
      <td>0.190738</td>
      <td>0.150360</td>
      <td>0.286298</td>
      <td>0.155098</td>
      <td>0.400742</td>
      <td>0.119984</td>
      <td>0.037748</td>
      <td>0.127941</td>
      <td>1.000000</td>
      <td>0.056399</td>
      <td>-0.081383</td>
      <td>0.084171</td>
      <td>0.049945</td>
      <td>0.079879</td>
      <td>0.077804</td>
      <td>0.027924</td>
      <td>0.078443</td>
      <td>-0.007124</td>
      <td>-0.005260</td>
      <td>0.009551</td>
      <td>0.047402</td>
      <td>0.055898</td>
      <td>0.119925</td>
      <td>0.097700</td>
      <td>0.103271</td>
      <td>0.073276</td>
    </tr>
    <tr>
      <th>average_review_age</th>
      <td>0.139108</td>
      <td>0.055847</td>
      <td>-0.080443</td>
      <td>-0.034258</td>
      <td>0.189623</td>
      <td>0.010070</td>
      <td>-0.125645</td>
      <td>0.064098</td>
      <td>0.056399</td>
      <td>1.000000</td>
      <td>0.192355</td>
      <td>0.003662</td>
      <td>0.032199</td>
      <td>0.031577</td>
      <td>0.028122</td>
      <td>0.218990</td>
      <td>0.820888</td>
      <td>0.243377</td>
      <td>0.261623</td>
      <td>0.377335</td>
      <td>0.030324</td>
      <td>0.035531</td>
      <td>-0.000525</td>
      <td>0.050846</td>
      <td>-0.024121</td>
      <td>-0.041140</td>
    </tr>
    <tr>
      <th>average_review_length</th>
      <td>0.037369</td>
      <td>-0.079183</td>
      <td>-0.116295</td>
      <td>-0.037712</td>
      <td>0.003850</td>
      <td>0.004748</td>
      <td>-0.277081</td>
      <td>0.046331</td>
      <td>-0.081383</td>
      <td>0.192355</td>
      <td>1.000000</td>
      <td>-0.133078</td>
      <td>0.027662</td>
      <td>0.027976</td>
      <td>0.059979</td>
      <td>0.083495</td>
      <td>0.178872</td>
      <td>0.112397</td>
      <td>0.088888</td>
      <td>0.168261</td>
      <td>0.000789</td>
      <td>0.004780</td>
      <td>0.013002</td>
      <td>-0.004609</td>
      <td>-0.016869</td>
      <td>0.006024</td>
    </tr>
    <tr>
      <th>average_review_sentiment</th>
      <td>0.097188</td>
      <td>0.073806</td>
      <td>0.130448</td>
      <td>0.054699</td>
      <td>0.089349</td>
      <td>0.076265</td>
      <td>0.782187</td>
      <td>0.086728</td>
      <td>0.084171</td>
      <td>0.003662</td>
      <td>-0.133078</td>
      <td>1.000000</td>
      <td>0.026948</td>
      <td>0.079057</td>
      <td>0.035839</td>
      <td>0.064738</td>
      <td>0.083046</td>
      <td>0.064385</td>
      <td>0.045517</td>
      <td>0.099804</td>
      <td>0.025967</td>
      <td>0.036676</td>
      <td>-0.003620</td>
      <td>0.056595</td>
      <td>0.067912</td>
      <td>0.044696</td>
    </tr>
    <tr>
      <th>number_funny_votes</th>
      <td>0.117472</td>
      <td>0.060658</td>
      <td>0.060595</td>
      <td>0.082213</td>
      <td>0.073215</td>
      <td>0.548164</td>
      <td>0.001320</td>
      <td>0.071131</td>
      <td>0.049945</td>
      <td>0.032199</td>
      <td>0.027662</td>
      <td>0.026948</td>
      <td>1.000000</td>
      <td>0.725554</td>
      <td>0.900795</td>
      <td>0.045171</td>
      <td>0.054688</td>
      <td>0.028421</td>
      <td>0.020624</td>
      <td>0.034570</td>
      <td>0.360497</td>
      <td>0.444257</td>
      <td>0.048625</td>
      <td>0.507570</td>
      <td>0.103491</td>
      <td>0.325476</td>
    </tr>
    <tr>
      <th>number_cool_votes</th>
      <td>0.188598</td>
      <td>0.113262</td>
      <td>0.114094</td>
      <td>0.147320</td>
      <td>0.119422</td>
      <td>0.860767</td>
      <td>0.043375</td>
      <td>0.129165</td>
      <td>0.079879</td>
      <td>0.031577</td>
      <td>0.027976</td>
      <td>0.079057</td>
      <td>0.725554</td>
      <td>1.000000</td>
      <td>0.863073</td>
      <td>0.077186</td>
      <td>0.077668</td>
      <td>0.050303</td>
      <td>0.035827</td>
      <td>0.061395</td>
      <td>0.560654</td>
      <td>0.684175</td>
      <td>0.072980</td>
      <td>0.777985</td>
      <td>0.178104</td>
      <td>0.554507</td>
    </tr>
    <tr>
      <th>number_useful_votes</th>
      <td>0.165775</td>
      <td>0.083832</td>
      <td>0.094000</td>
      <td>0.120622</td>
      <td>0.098990</td>
      <td>0.746949</td>
      <td>-0.000066</td>
      <td>0.115583</td>
      <td>0.077804</td>
      <td>0.028122</td>
      <td>0.059979</td>
      <td>0.035839</td>
      <td>0.900795</td>
      <td>0.863073</td>
      <td>1.000000</td>
      <td>0.038893</td>
      <td>0.061881</td>
      <td>0.016645</td>
      <td>0.006016</td>
      <td>0.020459</td>
      <td>0.450894</td>
      <td>0.556973</td>
      <td>0.091650</td>
      <td>0.649913</td>
      <td>0.149820</td>
      <td>0.441297</td>
    </tr>
    <tr>
      <th>average_number_friends</th>
      <td>0.015261</td>
      <td>0.016557</td>
      <td>0.028307</td>
      <td>0.015937</td>
      <td>0.087231</td>
      <td>0.026206</td>
      <td>-0.007629</td>
      <td>-0.025522</td>
      <td>0.027924</td>
      <td>0.218990</td>
      <td>0.083495</td>
      <td>0.064738</td>
      <td>0.045171</td>
      <td>0.077186</td>
      <td>0.038893</td>
      <td>1.000000</td>
      <td>0.315304</td>
      <td>0.781161</td>
      <td>0.545940</td>
      <td>0.525380</td>
      <td>0.053568</td>
      <td>0.056955</td>
      <td>0.045507</td>
      <td>0.060506</td>
      <td>0.004445</td>
      <td>0.010809</td>
    </tr>
    <tr>
      <th>average_days_on_yelp</th>
      <td>0.129901</td>
      <td>0.045057</td>
      <td>-0.045849</td>
      <td>0.000448</td>
      <td>0.176133</td>
      <td>0.050451</td>
      <td>-0.038061</td>
      <td>0.048850</td>
      <td>0.078443</td>
      <td>0.820888</td>
      <td>0.178872</td>
      <td>0.083046</td>
      <td>0.054688</td>
      <td>0.077668</td>
      <td>0.061881</td>
      <td>0.315304</td>
      <td>1.000000</td>
      <td>0.320788</td>
      <td>0.345481</td>
      <td>0.467893</td>
      <td>0.052168</td>
      <td>0.060782</td>
      <td>0.014544</td>
      <td>0.078031</td>
      <td>0.000783</td>
      <td>-0.006241</td>
    </tr>
    <tr>
      <th>average_number_fans</th>
      <td>0.017794</td>
      <td>0.024901</td>
      <td>0.018120</td>
      <td>0.023913</td>
      <td>0.104221</td>
      <td>0.000474</td>
      <td>-0.031141</td>
      <td>0.001131</td>
      <td>-0.007124</td>
      <td>0.243377</td>
      <td>0.112397</td>
      <td>0.064385</td>
      <td>0.028421</td>
      <td>0.050303</td>
      <td>0.016645</td>
      <td>0.781161</td>
      <td>0.320788</td>
      <td>1.000000</td>
      <td>0.798637</td>
      <td>0.625891</td>
      <td>0.029287</td>
      <td>0.031803</td>
      <td>0.030841</td>
      <td>0.027903</td>
      <td>0.002738</td>
      <td>0.001965</td>
    </tr>
    <tr>
      <th>average_review_count</th>
      <td>0.026846</td>
      <td>0.040692</td>
      <td>0.031203</td>
      <td>0.044006</td>
      <td>0.122982</td>
      <td>-0.002576</td>
      <td>-0.066572</td>
      <td>0.010618</td>
      <td>-0.005260</td>
      <td>0.261623</td>
      <td>0.088888</td>
      <td>0.045517</td>
      <td>0.020624</td>
      <td>0.035827</td>
      <td>0.006016</td>
      <td>0.545940</td>
      <td>0.345481</td>
      <td>0.798637</td>
      <td>1.000000</td>
      <td>0.687701</td>
      <td>0.029392</td>
      <td>0.031895</td>
      <td>0.032118</td>
      <td>0.025542</td>
      <td>0.004597</td>
      <td>0.002460</td>
    </tr>
    <tr>
      <th>average_number_years_elite</th>
      <td>0.099141</td>
      <td>0.094233</td>
      <td>0.083062</td>
      <td>0.082863</td>
      <td>0.210487</td>
      <td>0.014712</td>
      <td>-0.064419</td>
      <td>0.063990</td>
      <td>0.009551</td>
      <td>0.377335</td>
      <td>0.168261</td>
      <td>0.099804</td>
      <td>0.034570</td>
      <td>0.061395</td>
      <td>0.020459</td>
      <td>0.525380</td>
      <td>0.467893</td>
      <td>0.625891</td>
      <td>0.687701</td>
      <td>1.000000</td>
      <td>0.045112</td>
      <td>0.051960</td>
      <td>0.059031</td>
      <td>0.049284</td>
      <td>0.035118</td>
      <td>0.019713</td>
    </tr>
    <tr>
      <th>weekday_checkins</th>
      <td>0.094398</td>
      <td>0.068960</td>
      <td>0.082474</td>
      <td>0.107467</td>
      <td>0.057877</td>
      <td>0.567452</td>
      <td>0.004130</td>
      <td>0.053162</td>
      <td>0.047402</td>
      <td>0.030324</td>
      <td>0.000789</td>
      <td>0.025967</td>
      <td>0.360497</td>
      <td>0.560654</td>
      <td>0.450894</td>
      <td>0.053568</td>
      <td>0.052168</td>
      <td>0.029287</td>
      <td>0.029392</td>
      <td>0.045112</td>
      <td>1.000000</td>
      <td>0.947118</td>
      <td>0.039370</td>
      <td>0.802160</td>
      <td>0.088600</td>
      <td>0.262576</td>
    </tr>
    <tr>
      <th>weekend_checkins</th>
      <td>0.131175</td>
      <td>0.079808</td>
      <td>0.093579</td>
      <td>0.126861</td>
      <td>0.081321</td>
      <td>0.699631</td>
      <td>0.007863</td>
      <td>0.076183</td>
      <td>0.055898</td>
      <td>0.035531</td>
      <td>0.004780</td>
      <td>0.036676</td>
      <td>0.444257</td>
      <td>0.684175</td>
      <td>0.556973</td>
      <td>0.056955</td>
      <td>0.060782</td>
      <td>0.031803</td>
      <td>0.031895</td>
      <td>0.051960</td>
      <td>0.947118</td>
      <td>1.000000</td>
      <td>0.042727</td>
      <td>0.875169</td>
      <td>0.109552</td>
      <td>0.346862</td>
    </tr>
    <tr>
      <th>average_tip_length</th>
      <td>0.098037</td>
      <td>0.121948</td>
      <td>0.144163</td>
      <td>0.104742</td>
      <td>0.129212</td>
      <td>0.094133</td>
      <td>-0.052899</td>
      <td>0.084098</td>
      <td>0.119925</td>
      <td>-0.000525</td>
      <td>0.013002</td>
      <td>-0.003620</td>
      <td>0.048625</td>
      <td>0.072980</td>
      <td>0.091650</td>
      <td>0.045507</td>
      <td>0.014544</td>
      <td>0.030841</td>
      <td>0.032118</td>
      <td>0.059031</td>
      <td>0.039370</td>
      <td>0.042727</td>
      <td>1.000000</td>
      <td>0.081828</td>
      <td>0.081929</td>
      <td>0.054535</td>
    </tr>
    <tr>
      <th>number_tips</th>
      <td>0.208856</td>
      <td>0.156536</td>
      <td>0.147115</td>
      <td>0.173542</td>
      <td>0.119632</td>
      <td>0.844978</td>
      <td>0.014038</td>
      <td>0.134832</td>
      <td>0.097700</td>
      <td>0.050846</td>
      <td>-0.004609</td>
      <td>0.056595</td>
      <td>0.507570</td>
      <td>0.777985</td>
      <td>0.649913</td>
      <td>0.060506</td>
      <td>0.078031</td>
      <td>0.027903</td>
      <td>0.025542</td>
      <td>0.049284</td>
      <td>0.802160</td>
      <td>0.875169</td>
      <td>0.081828</td>
      <td>1.000000</td>
      <td>0.190528</td>
      <td>0.450343</td>
    </tr>
    <tr>
      <th>average_caption_length</th>
      <td>0.305570</td>
      <td>0.291413</td>
      <td>0.180468</td>
      <td>0.258938</td>
      <td>0.170171</td>
      <td>0.224983</td>
      <td>0.000040</td>
      <td>0.282823</td>
      <td>0.103271</td>
      <td>-0.024121</td>
      <td>-0.016869</td>
      <td>0.067912</td>
      <td>0.103491</td>
      <td>0.178104</td>
      <td>0.149820</td>
      <td>0.004445</td>
      <td>0.000783</td>
      <td>0.002738</td>
      <td>0.004597</td>
      <td>0.035118</td>
      <td>0.088600</td>
      <td>0.109552</td>
      <td>0.081929</td>
      <td>0.190528</td>
      <td>1.000000</td>
      <td>0.249235</td>
    </tr>
    <tr>
      <th>number_pics</th>
      <td>0.252523</td>
      <td>0.175058</td>
      <td>0.109552</td>
      <td>0.210583</td>
      <td>0.143570</td>
      <td>0.610889</td>
      <td>0.001727</td>
      <td>0.231242</td>
      <td>0.073276</td>
      <td>-0.041140</td>
      <td>0.006024</td>
      <td>0.044696</td>
      <td>0.325476</td>
      <td>0.554507</td>
      <td>0.441297</td>
      <td>0.010809</td>
      <td>-0.006241</td>
      <td>0.001965</td>
      <td>0.002460</td>
      <td>0.019713</td>
      <td>0.262576</td>
      <td>0.346862</td>
      <td>0.054535</td>
      <td>0.450343</td>
      <td>0.249235</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



To further visualize these relationships, we can plot certain features against our dependent variable, the Yelp rating. In the cell below we have provided the code to import Matplotlib. We can use Matplotlib's `.scatter()` method with the below syntax to plot what these correlations look like:

```python
plt.scatter(x_values_to_plot, y_values_to_plot, alpha=blending_val)
```

* `x_values_to_plot` are the values to be plotted along the x-axis
* `y_values_to_plot` are the values to be plotted along the y-axis
* `alpha=blending_val` is the blending value, or how transparent (0) or opaque (1) a plotted point is. This will help us distinguish areas of the plot with high point densities and low point densities

Plot the three features that correlate most with Yelp rating (`average_review_sentiment`, `average_review_length`, `average_review_age`) against `stars`, our Yelp rating. Then plot a lowly correlating feature, such as `number_funny_votes`, against `stars`.

>What is `average_review_sentiment`, you ask? `average_review_sentiment` is the average sentiment score for all reviews on a business' Yelp page. The sentiment score for a review was calculated using the sentiment analysis tool [VADER](https://github.com/cjhutto/vaderSentiment). VADER uses a labeled set of positive and negative words, along with codified rules of grammar, to estimate how positive or negative a statement is. Scores range from `-1`, most negative, to `+1`, most positive, with a score of `0` indicating a neutral statement. While not perfect, VADER does a good job at guessing the sentiment of text data!

What kind of relationships do you see from the plots? Do you think these variables are good or bad features for our Yelp rating prediction model?


```python
from matplotlib import pyplot as plt

# plot average_review_sentiment against stars here
plt.scatter(df['average_review_sentiment'], df['stars'], alpha=0.5)
plt.show()
```


![png](output_32_0.png)



```python
# plot average_review_length against stars here
plt.scatter(df['average_review_length'], df['stars'], alpha=0.5)
```




    <matplotlib.collections.PathCollection at 0x2781010cf10>




![png](output_33_1.png)



```python
# plot average_review_age against stars here
plt.scatter(df['average_review_age'], df['stars'], alpha=0.5)
```




    <matplotlib.collections.PathCollection at 0x27810129a60>




![png](output_34_1.png)



```python
# plot number_funny_votes against stars here
plt.scatter(df['number_funny_votes'], df['stars'], alpha=0.5)
```




    <matplotlib.collections.PathCollection at 0x27810144580>




![png](output_35_1.png)


Why do you think `average_review_sentiment` correlates so well with Yelp rating?

## Data Selection

In order to put our data into a Linear Regression model, we need to separate out our features to model on and the Yelp ratings. From our correlation analysis we saw that the three features with the strongest correlations to Yelp rating are `average_review_sentiment`, `average_review_length`, and `average_review_age`. Since we want to dig a little deeper than `average_review_sentiment`, which understandably has a very high correlation with Yelp rating, let's choose to create our first model with `average_review_length` and `average_review_age` as features.

Pandas lets us select one column of a DataFrame with the following syntax:

```python
subset_of_data = df['feature_to_select']
```
Pandas also lets us select multiple columns from a DataFrame with this syntax:

```python
subset_of_data = df[list_of_features_to_select]
```
Create a new DataFrame `features` that contains the columns we want to model on: `average_review_length` and `average_review_age`. Then create another DataFrame `ratings` that stores the value we want to predict, Yelp rating, or `stars` in `df`.


```python
features = df[['average_review_length', 'average_review_age']]
ratings = df['stars']
```

## Split the Data into Training and Testing Sets

We are just about ready to model! But first, we need to break our data into a training set and a test set so we can evaluate how well our model performs. We'll use scikit-learn's `train_test_split` function to do this split, which is provided in the cell below. This function takes two required parameters: the data, or our features, followed by our dependent variable, in our case the Yelp rating. Set the optional parameter `test_size` to be `0.2`. Finally, set the optional parameter `random_state` to `1`. This will make it so your data is split in the same way as the data in our solution code. 

Remember, this function returns 4 items in this order:
1. The training data (features), which we can assign to `X_train`
2. The testing data (features), which we can assign to `X_test`
3. The training dependent variable (Yelp rating), which we can assign to `y_train`
4. The testing dependent variable (Yelp rating), which we can assign to `y_test`


```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, ratings, test_size=0.2, random_state=1)
```

## Create and Train the Model

Now that our data is split into training and testing sets, we can finally model! In the cell below we have provided the code to import `LinearRegression` from scikit-learn's `linear_model` module. Create a new `LinearRegression` object named model. The `.fit()` method will fit our Linear Regression model to our training data and calculate the coefficients for our features. Call the `.fit()` method on `model` with `X_train` and `y_train` as parameters. Just like that our model has now been trained on our training data!


```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)



## Evaluate and Understand the Model

Now we can evaluate our model in a variety of ways. The first way will be by using the `.score()` method, which provides the R^2 value for our model. Remember, R^2 is the coefficient of determination, or a measure of how much of the variance in our dependent variable, the predicted Yelp rating, is explained by our independent variables, our feature data. R^2 values range from `0` to `1`, with `0` indicating that the created model does not fit our data at all, and with `1` indicating the model perfectly fits our feature data. Call `.score()` on our model with `X_train` and `y_train` as parameters to calculate our training R^2 score. Then call `.score()` again on model with `X_test` and `y_test` as parameters to calculate R^2 for our testing data. What do these R^2 values say about our model? Do you think these features alone are able to effectively predict Yelp ratings?


```python
#model.score(X_train, y_train)
model.score(X_test, y_test)
```




    0.08083081210060561



After all that hard work, we can finally take a look at the coefficients on our different features! The model has an attribute `.coef_` which is an array of the feature coefficients determined by fitting our model to the training data. To make it easier for you to see which feature corresponds to which coefficient, we have provided some code in the cell that `zip`s together a list of our features with the coefficients and sorts them in descending order from most predictive to least predictive.


```python
sorted(list(zip(['average_review_length','average_review_age'],model.coef_)),key = lambda x: abs(x[1]),reverse=True)
```




    [('average_review_length', -0.0009977176852074524),
     ('average_review_age', -0.00011621626836366473)]



Lastly we can calculate the predicted Yelp ratings for our testing data and compare them to their actual Yelp ratings! Our model has a `.predict()` method which uses the model's coefficients to calculate the predicted Yelp rating. Call `.predict()` on `X_test` and assign the values to `y_predicted`. Use Matplotlib to plot `y_test` vs `y_predicted`. For a perfect linear regression model we would expect to see the data plotted along the line `y = x`, indicating homoscedasticity. Is this the case? If not, why not? Would you call this model heteroscedastic or homoscedastic?


```python
y_predicted = model.predict(X_test)
plt.plot(y_test, y_predicted)
```




    [<matplotlib.lines.Line2D at 0x2781154cd30>]




![png](output_48_1.png)


## Define Different Subsets of Data

After evaluating the first model, you can see that `average_review_length` and `average_review_age` alone are not the best predictors for Yelp rating. Let's go do some more modeling with different subsets of features and see if we can achieve a more accurate model! In the cells below we have provided different lists of subsets of features that we will model with and evaluate. What other subsets of features would you want to test? Why do you think those feature sets are more predictive of Yelp rating than others? Create at least one more subset of features that you want to predict Yelp ratings from.


```python
# subset of only average review sentiment
sentiment = ['average_review_sentiment']
```


```python
# subset of all features that have a response range [0,1]
binary_features = ['alcohol?','has_bike_parking','takes_credit_cards','good_for_kids','take_reservations','has_wifi']
```


```python
# subset of all features that vary on a greater range than [0,1]
numeric_features = ['review_count','price_range','average_caption_length','number_pics','average_review_age','average_review_length','average_review_sentiment','number_funny_votes','number_cool_votes','number_useful_votes','average_tip_length','number_tips','average_number_friends','average_days_on_yelp','average_number_fans','average_review_count','average_number_years_elite','weekday_checkins','weekend_checkins']
```


```python
# all features
all_features = binary_features + numeric_features
```


```python
# add your own feature subset here
feature_subset = ['average_review_sentiment', 'average_review_age','average_review_length']
```

## Further Modeling

Now that we have lists of different feature subsets, we can create new models from them. In order to more easily compare the performance of these new models, we have created a function for you below called `model_these_features()`. This function replicates the model building process you just completed with our first model! Take some time to review how the function works, analyzing it line by line. Fill in the empty comments with an explanation of the task the code beneath it is performing.


```python
import numpy as np

# take a list of features to model as a parameter
def model_these_features(feature_list):
    
    # 
    ratings = df.loc[:,'stars']
    features = df.loc[:,feature_list]
    
    # 
    X_train, X_test, y_train, y_test = train_test_split(features, ratings, test_size = 0.2, random_state = 1)
    
    # don't worry too much about these lines, just know that they allow the model to work when
    # we model on just one feature instead of multiple features. Trust us on this one :)
    if len(X_train.shape) < 2:
        X_train = np.array(X_train).reshape(-1,1)
        X_test = np.array(X_test).reshape(-1,1)
    
    # 
    model = LinearRegression()
    model.fit(X_train,y_train)
    
    # 
    print('Train Score:', model.score(X_train,y_train))
    print('Test Score:', model.score(X_test,y_test))
    
    # print the model features and their corresponding coefficients, from most predictive to least predictive
    print(sorted(list(zip(feature_list,model.coef_)),key = lambda x: abs(x[1]),reverse=True))
    
    # 
    y_predicted = model.predict(X_test)
    
    # 
    plt.scatter(y_test,y_predicted)
    plt.xlabel('Yelp Rating')
    plt.ylabel('Predicted Yelp Rating')
    plt.ylim(1,5)
    plt.show()
```

Once you feel comfortable with the steps of the function, run models on the following subsets of data using `model_these_features()`:
* `sentiment`: only `average_review_sentiment`
* `binary_features`: all features that have a response range [0,1]
* `numeric_features`: all features that vary on a greater range than [0,1]
* `all_features`: all features
* `feature_subset`: your own feature subset

How does changing the feature sets affect the model's R^2 value? Which features are most important to predicting Yelp rating in the different models? Which models appear more or less homoscedastic?


```python
# create a model on sentiment here
model_these_features(sentiment)
```

    Train Score: 0.6118980950438655
    Test Score: 0.6114021046919492
    [('average_review_sentiment', 2.3033908433749612)]
    


![png](output_59_1.png)



```python
# create a model on all binary features here
model_these_features(binary_features)
```

    Train Score: 0.012223180709591164
    Test Score: 0.010119542202269072
    [('has_bike_parking', 0.19003008208038988), ('alcohol?', -0.14549670708138188), ('has_wifi', -0.1318739757776259), ('good_for_kids', -0.08632485990337416), ('takes_credit_cards', 0.071755364921953), ('take_reservations', 0.04526558530451624)]
    


![png](output_60_1.png)



```python
# create a model on all numeric features here
model_these_features(numeric_features)
```

    Train Score: 0.6734992593766658
    Test Score: 0.6713318798120151
    [('average_review_sentiment', 2.2721076642095714), ('price_range', -0.08046080962701326), ('average_number_years_elite', -0.07190366288054215), ('average_caption_length', -0.00334706600778448), ('number_pics', -0.0029565028128954863), ('number_tips', -0.0015953050789045838), ('number_cool_votes', 0.0011468839227079775), ('average_number_fans', 0.0010510602097412254), ('average_review_length', -0.0005813655692093357), ('average_tip_length', -0.0005322032063459733), ('number_useful_votes', -0.0002320378475871201), ('average_review_count', -0.0002243170289501482), ('average_review_age', -0.00016930608165055923), ('average_days_on_yelp', 0.00012878025876674438), ('weekday_checkins', 5.91858075448613e-05), ('weekend_checkins', -5.518176206999151e-05), ('average_number_friends', 4.8269921116315975e-05), ('review_count', -3.483483763748981e-05), ('number_funny_votes', -7.884395673808679e-06)]
    


![png](output_61_1.png)



```python
# create a model on all features here
model_these_features(all_features)
```

    Train Score: 0.6807828861895334
    Test Score: 0.6782129045869247
    [('average_review_sentiment', 2.2808456996623825), ('alcohol?', -0.14991498593470284), ('has_wifi', -0.12155382629261363), ('good_for_kids', -0.1180781442201382), ('price_range', -0.06486730150043177), ('average_number_years_elite', -0.06278939713895364), ('has_bike_parking', 0.027296969912292805), ('takes_credit_cards', 0.024451837853653652), ('take_reservations', 0.014134559172969846), ('number_pics', -0.0013133612300796843), ('average_number_fans', 0.0010267986822656814), ('number_cool_votes', 0.0009723722734409323), ('number_tips', -0.0008546563320873921), ('average_caption_length', -0.0006472749798195219), ('average_review_length', -0.0005896257920272453), ('average_tip_length', -0.00042052175034042557), ('number_useful_votes', -0.00027150641256153645), ('average_review_count', -0.000233983569025111), ('average_review_age', -0.00015776544111324774), ('average_days_on_yelp', 0.0001232614766288456), ('review_count', 0.00010112259377362226), ('weekend_checkins', -9.239617469638006e-05), ('weekday_checkins', 6.153909123144103e-05), ('number_funny_votes', 4.8479351025075246e-05), ('average_number_friends', 2.069584037372081e-05)]
    


![png](output_62_1.png)



```python
# create a model on your feature subset here
model_these_features(feature_subset)
```

    Train Score: 0.6520510292564032
    Test Score: 0.6495675480094902
    [('average_review_sentiment', 2.243030310441711), ('average_review_length', -0.0005978300178804316), ('average_review_age', -0.0001520993682315242)]
    


![png](output_63_1.png)


## Danielle's Delicious Delicacies' Debut

You've loaded the data, cleaned it, modeled it, and evaluated it. You're tired, but glowing with pride after all the hard work. You close your eyes and can clearly see opening day of Danielle's Delicious Delicacies with a line out the door. But what will your Yelp rating be? Let's use our model to make a prediction.

Our best model was the model using all features, so we'll work with this model again. In the cell below print `all_features` to get a reminder of what features we are working with.


```python
print(all_features)
```

    ['alcohol?', 'has_bike_parking', 'takes_credit_cards', 'good_for_kids', 'take_reservations', 'has_wifi', 'review_count', 'price_range', 'average_caption_length', 'number_pics', 'average_review_age', 'average_review_length', 'average_review_sentiment', 'number_funny_votes', 'number_cool_votes', 'number_useful_votes', 'average_tip_length', 'number_tips', 'average_number_friends', 'average_days_on_yelp', 'average_number_fans', 'average_review_count', 'average_number_years_elite', 'weekday_checkins', 'weekend_checkins']
    

Run the cell below to grab all the features and retrain our model on them.


```python
features = df.loc[:,all_features]
ratings = df.loc[:,'stars']
X_train, X_test, y_train, y_test = train_test_split(features, ratings, test_size = 0.2, random_state = 1)
model = LinearRegression()
model.fit(X_train,y_train)
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)



To give you some perspective on the restaurants already out there, we have provided the mean, minimum, and maximum values for each feature below. Will Danielle's Delicious Delicacies be just another average restaurant, or will it be a 5 star behemoth amongst the masses?


```python
pd.DataFrame(list(zip(features.columns,features.describe().loc['mean'],features.describe().loc['min'],features.describe().loc['max'])),columns=['Feature','Mean','Min','Max'])
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
      <th>Feature</th>
      <th>Mean</th>
      <th>Min</th>
      <th>Max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>alcohol?</td>
      <td>0.140610</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>has_bike_parking</td>
      <td>0.350692</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>takes_credit_cards</td>
      <td>0.700243</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>good_for_kids</td>
      <td>0.279029</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>take_reservations</td>
      <td>0.106086</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>has_wifi</td>
      <td>0.134968</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>review_count</td>
      <td>31.797310</td>
      <td>3.000000</td>
      <td>7968.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>price_range</td>
      <td>1.035855</td>
      <td>0.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>average_caption_length</td>
      <td>2.831829</td>
      <td>0.000000</td>
      <td>140.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>number_pics</td>
      <td>1.489939</td>
      <td>0.000000</td>
      <td>1150.000000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>average_review_age</td>
      <td>1175.501021</td>
      <td>71.555556</td>
      <td>4727.333333</td>
    </tr>
    <tr>
      <th>11</th>
      <td>average_review_length</td>
      <td>596.463567</td>
      <td>62.400000</td>
      <td>4229.000000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>average_review_sentiment</td>
      <td>0.554935</td>
      <td>-0.995200</td>
      <td>0.996575</td>
    </tr>
    <tr>
      <th>13</th>
      <td>number_funny_votes</td>
      <td>15.617091</td>
      <td>0.000000</td>
      <td>36822.000000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>number_cool_votes</td>
      <td>18.495973</td>
      <td>0.000000</td>
      <td>6572.000000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>number_useful_votes</td>
      <td>43.515279</td>
      <td>0.000000</td>
      <td>38357.000000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>average_tip_length</td>
      <td>45.643426</td>
      <td>0.000000</td>
      <td>500.000000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>number_tips</td>
      <td>6.285217</td>
      <td>0.000000</td>
      <td>3581.000000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>average_number_friends</td>
      <td>105.132000</td>
      <td>1.000000</td>
      <td>4219.000000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>average_days_on_yelp</td>
      <td>2005.367009</td>
      <td>76.000000</td>
      <td>4860.000000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>average_number_fans</td>
      <td>11.590148</td>
      <td>0.000000</td>
      <td>1174.666667</td>
    </tr>
    <tr>
      <th>21</th>
      <td>average_review_count</td>
      <td>122.110660</td>
      <td>0.666667</td>
      <td>6335.000000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>average_number_years_elite</td>
      <td>0.923313</td>
      <td>0.000000</td>
      <td>10.666667</td>
    </tr>
    <tr>
      <th>23</th>
      <td>weekday_checkins</td>
      <td>45.385094</td>
      <td>0.000000</td>
      <td>73830.000000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>weekend_checkins</td>
      <td>49.612515</td>
      <td>0.000000</td>
      <td>64647.000000</td>
    </tr>
  </tbody>
</table>
</div>



Based on your plans for the restaurant, how you expect your customers to post on your Yelp page, and the values above, fill in the blanks in the NumPy array below with your desired values. The first blank corresponds with the feature at `index=0` in the DataFrame above, `alcohol?`, and the last blank corresponds to the feature at ``index=24``, `weekend_checkins`. Make sure to enter either `0` or `1` for all binary features, and if you aren't sure of what value to put for a feature, select the mean from the DataFrame above. After you enter the values, run the prediction cell below to receive your Yelp rating! How is Danielle's Delicious Delicacies debut going to be?


```python
danielles_delicious_delicacies = np.array([1,1,1,0,0,1,20,2,10,10,100,120,0.5,200,250,100,100,20,200,1,150,100,1,100,200]).reshape(1,-1)
```


```python
model.predict(danielles_delicious_delicacies)
```




    array([3.76893534])



## Next Steps

You have successfully built a linear regression model that predicts a restaurant's Yelp rating! As you have seen, it can be pretty hard to predict a rating like this even when we have a plethora of data. What other questions come to your mind when you see the data we have? What insights do you think could come from a different kind of analysis? Here are some ideas to ponder:

* Can we predict the cuisine of a restaurant based on the users that review it?
* What restaurants are similar to each other in ways besides cuisine?
* Are there different restaurant vibes, and what kind of restaurants fit these conceptions?
* How does social media status affect a restaurant's credibility and visibility?

As you progress further into the field of data science, you will be able to create models that address these questions and many more! But in the meantime, get back to working on that burgeoning restaurant business plan.
