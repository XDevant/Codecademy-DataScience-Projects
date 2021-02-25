#!/usr/bin/env python
# coding: utf-8

# # Introduction
# In this project, you will act as a data visualization developer at Yahoo Finance!
# You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data.
# In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market.
# Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.
# 
# After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:
# 
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# 1. Import the modules that you'll be using in this project: matplotlib, pandas, seaborn

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# 2. Let's load the datasets and inspect them.

# Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`. 
# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits.
# This means this is the true closing stock price for a given business day.

netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks.head())

# Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.
# Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 

dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks.head())


# Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.

netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly.head())

# 3. Let's learn more about our data. Open the CSV files directly from the folder you downloaded for this project.
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 

# What year is represented in the data? Look out for the latest and earliest date.

# + Is the data represented by days, weeks, or months? 
# + In which ways are the files different? 
# + What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?


# 4. Let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. 

netflix_stocks.head()

# What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! 
# The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation.
# In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
# This means this is the column with the true closing price, so these data are very important.
# 
# Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. 
# Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.

netflix_stocks.rename(columns={'Adj Close':'Price'},inplace=True)
netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'},inplace=True)
dowjones_stocks.rename(columns={'Adj Close':'Price'},inplace=True)

netflix_stocks.head()
dowjones_stocks.head()
netflix_stocks_quarterly.head()

# 5. In this step, we will be visualizing the Netflix quarterly data! 
# We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017.
# Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!
# 
# 1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.
# 2. Use `sns.violinplot()` and pass in the following arguments:
# + The `Quarter` column as the `x` values
# + The `Price` column as your `y` values
# + The `netflix_stocks_quarterly` dataframe as your `data`
# 3. Improve the readability of the chart by adding a title of the plot. Add `"Distribution of 2017 Netflix Stock Prices by Quarter"` by using `ax.set_title()`
# 4. Change your `ylabel` to "Closing Stock Price"
# 5. Change your `xlabel` to "Business Quarters in 2017"
# 6. Be sure to show your plot!

ax = sns.violinplot()
sns.violinplot(data=netflix_stocks_quarterly, x='Quarter', y='Price')
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
plt.xlabel("Business Quarters in 2017")
plt.ylabel("Closing Stock Price")


# 6. Next, we will chart the EPS by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters.
# We will accomplish this using a scatter chart. 
# 
# 1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.
# 2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color
# 
# 3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.
# 4. Add a legend by using `plt.legend()` and passing in a list with two strings `["Actual", "Estimate"]`
# 
# 5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`
# 6. Assing "`"Earnings Per Share in Cents"` as the title of your plot.

x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

plt.scatter(x_positions, earnings_actual, color='red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='blue', alpha=0.5)
plt.xticks(x_positions, chart_labels)
plt.legend(["Actual", "Estimate"])
plt.title('Earnings Per Share in Cents')

# 7. Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side.
# We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).
# 
# As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. 
# 
# 1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars
# 2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data
# 3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars
# 4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data
# 5. Create a legend for your bar chart with the `labels` provided
# 6. Add a descriptive title for your chart with `plt.title()`
# 7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]

plt.bar(bars1_x, revenue_by_quarter)


# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

plt.bar(bars2_x, earnings_by_quarter)
plt.title('Earnings and Revenue')

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.xticks(middle_x, quarter_labels)
plt.legend(labels)
plt.show()

# 8. In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017.
# We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively.
# - Assign "Netflix" as a title to this subplot. Hint: `ax1.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively.
# - Assign "Dow Jones" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`

# Left plot Netflix
plt.figure(figsize=(14,6))
ax1 = plt.subplot(1,2,1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xlabel("2017")
ax1.set_ylabel("Stock Price")
ax1.set_xticks(range(12))
ax1.set_xticklabels(['Jan','Fev','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#
# Right plot Dow Jones

ax2 = plt.subplot(1,2,2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Dow Jones')
ax2.set_xlabel("2017")
ax2.set_ylabel("Stock Price")
plt.subplots_adjust(wspace=.5)
ax2.set_xticks(range(12))
ax2.set_xticklabels(['Jan','Fev','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.show()




