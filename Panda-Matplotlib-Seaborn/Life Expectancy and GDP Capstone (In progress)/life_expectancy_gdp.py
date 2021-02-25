#!/usr/bin/env python
# coding: utf-8

# # Introduction
# For this project, you will act as a data researcher for the World Health Organization.
# You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)

# 1. Import Python Modules: matplotlib, pandas, seaborn

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# 2. Prep The Data

# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.

df = pd.read_csv('all_data.csv')
df.head()

# 3. Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer.
# You can open the CSV files directly from the folder you downloaded for this project.
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

df.Country.unique()

# What years are represented in the data?

df.Year.unique()

# 4. Tweak The DataFrame
# Look at the column names of the DataFrame `df` using `.head()`. 

df.head()

# What do you notice? The first two column names are one word each, and the third is five words long!
# `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.

df.rename(columns = {'Life expectancy at birth (years)': 'LEABY'}, inplace = True)
df.head()

# 5. Bar Charts To Compare Average
# To take a first high level look at both datasets, create a bar chart for each DataFrame:

# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 

plt.bar(range(len(df.Country)), df.GDP)
plt.show()

# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.

plt.bar(range(len(df.Country)), df.LEABY)
plt.show()

#  6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 

fig = plt.subplots(figsize=(15, 10)) 
sns.violinplot(data=df, x='Country', y='LEABY')
plt.show()

# 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.

f, ax = plt.subplots(figsize=(10, 15))
ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)
plt.ylabel("GDP in Trillions of U.S. Dollars")


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`

f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)
plt.ylabel("Life expectancy at birth in years")
plt.show()

# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose.
# In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.
#  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`.
# A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!

# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs

# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter

g = sns.FacetGrid(df, col='Year', hue='Country', col_wrap=4, height=3)
g = (g.map(plt.scatter, 'GDP', 'LEABY', edgecolor="w").add_legend())
plt.show()

# 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph.
 # That makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.

# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())
plt.show()

#  10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis.
# Change the color on your own! Be sure to show your plot.

g4 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g4 = (g4.map(plt.plot, "Year", "GDP").add_legend())
plt.show()



# 11. Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization.
# You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# 12. Create Blog Post

