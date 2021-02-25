#!/usr/bin/env python
# coding: utf-8

# # Capstone Project 1: MuscleHub AB Test

# 1: Get started with SQL
# Like most businesses, Janet keeps her data in a SQL database.  Normally, you'd download the data from her database to a csv file, and then load it into a Jupyter Notebook using Pandas.
# For this project, you'll have to access SQL in a slightly different way.  You'll be using a special Codecademy library that lets you type SQL queries directly into this Jupyter notebook.  You'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame.  Here's an example:

# This import only needs to happen once, at the beginning of the notebook
from codecademySQL import sql_query

# Here's an example where we save the data to a DataFrame
df = sql_query('''
SELECT *
FROM applications
LIMIT 5
''')

# 2: Get your dataset
# Janet of MuscleHub has a SQLite database, which contains several tables that will be helpful to you in this investigation:
# - `visits` contains information about potential gym customers who have visited MuscleHub
# - `fitness_tests` contains information about potential customers in "Group A", who were given a fitness test
# - `applications` contains information about any potential customers (both "Group A" and "Group B") who filled out an application.  Not everyone in `visits` will have filled out an application.
# - `purchases` contains information about customers who purchased a membership to MuscleHub.

sql_query('''
SELECT *
FROM visits
LIMIT 5
''')

sql_query('''
SELECT *
FROM fitness_tests
LIMIT 5
''')

sql_query('''
SELECT *
FROM applications
LIMIT 5
''')

sql_query('''
SELECT *
FROM purchases
LIMIT 5
''')


# We'd like to download a giant DataFrame containing all of this data.  You'll need to write a query that does the following things:
# 1. Not all visits in  `visits` occurred during the A/B test.  You'll only want to pull data where `visit_date` is on or after `7-1-17`.
# 2. You'll want to perform a series of `LEFT JOIN` commands to combine the four tables that we care about.  You'll need to perform the joins on `first_name`, `last_name`, and `email`.  Pull the following columns:
 # - `visits.first_name`
# - `visits.last_name`
# - `visits.gender`
# - `visits.email`
# - `visits.visit_date`
# - `fitness_tests.fitness_test_date`
# - `applications.application_date`
# - `purchases.purchase_date`
# 
# Save the result of this query to a variable called `df`.

df = sql_query('''SELECT visits.first_name,
    visits.last_name,
    visits.gender,
    visits.email,
    visits.visit_date,
    fitness_tests.fitness_test_date,
    applications.application_date,
    purchases.purchase_date
FROM visits
LEFT JOIN fitness_tests
  ON (visits.first_name = fitness_tests.first_name) 
  AND (visits.last_name = fitness_tests.last_name)
  AND (visits.email = fitness_tests.email)
LEFT JOIN applications
  ON (applications.first_name = visits.first_name) 
  AND (applications.last_name = visits.last_name)
  AND (applications.email = visits.email)
LEFT JOIN purchases
  ON (applications.first_name = purchases.first_name) 
  AND (applications.last_name = purchases.last_name)
  AND (applications.email = purchases.email)
WHERE (visits.visit_date NOT LIKE '5-_-17') AND (visits.visit_date NOT LIKE '6-_-17') 
    AND (visits.visit_date NOT LIKE '5-__-17') AND (visits.visit_date NOT LIKE '6-__-17')
''')

# 3: Investigate the A and B groups
# - `import pandas as pd`
# - `from matplotlib import pyplot as plt`

import pandas as pd
from matplotlib import pyplot as plt

# We're going to add some columns to `df` to help us with our analysis.
# Start by adding a column called `ab_test_group`.  It should be `A` if `fitness_test_date` is not `None`, and `B` if `fitness_test_date` is `None`.

df['ab_test_group'] = df.apply(lambda row: 'A' if row.fitness_test_date is not None else 'B', axis=1)
df

# Let's do a quick sanity check that Janet split her visitors such that about half are in A and half are in B.
# Start by using `groupby` to count how many users are in each `ab_test_group`.  Save the results to `ab_counts`.

ab_counts = df.groupby('ab_test_group').first_name.count().reset_index()
ab_counts

# We'll want to include this information in our presentation.  Let's create a pie cart using `plt.pie`.  Make sure to include:
# - Use `plt.axis('equal')` so that your pie chart looks nice
# - Add a legend labeling `A` and `B`
# - Use `autopct` to label the percentage of each group
# - Save your figure as `ab_test_pie_chart.png`

plt.pie(ab_counts.first_name, autopct='%0.2f%%')
plt.axis('equal')
plt.legend(ab_counts.ab_test_group)
plt.savefig('ab_test_pie_chart.png')
plt.show()


# 4: Who picks up an application?
# Recall that the sign-up process for MuscleHub has several steps:
# 1. Take a fitness test with a personal trainer (only Group A)
# 2. Fill out an application for the gym
# 3. Send in their payment for their first month's membership
# 
# Let's examine how many people make it to Step 2, filling out an application.
# Start by creating a new column in `df` called `is_application` which is `Application` if `application_date` is not `None` and `No Application`, otherwise.

df['is_application'] = df.apply(lambda row: 'Application' if row.application_date is not None 
                                else 'No Application', axis=1)
df

# Now, using `groupby`, count how many people from Group A and Group B either do or don't pick up an application.  You'll want to group by `ab_test_group` and `is_application`.  Save this new DataFrame as `app_counts`

app_counts = df.groupby(['ab_test_group', 'is_application']).first_name.count().reset_index()
app_counts.head()

# We're going to want to calculate the percent of people in each group who complete an application.  It's going to be much easier to do this if we pivot `app_counts` such that:
# - The `index` is `ab_test_group`
# - The `columns` are `is_application`
# Perform this pivot and save it to the variable `app_pivot`.  Remember to call `reset_index()` at the end of the pivot!

app_pivot = app_counts.pivot(index='ab_test_group',
                             columns='is_application',
                             values='first_name').reset_index()
app_pivot


# Define a new column called `Total`, which is the sum of `Application` and `No Application`.

app_pivot['Total'] = app_pivot.apply(lambda row: row.Application+row['No Application'], axis=1)
app_pivot


# Calculate another column called `Percent with Application`, which is equal to `Application` divided by `Total`.

app_pivot['Percent with Application'] = app_pivot.apply(lambda row: row.Application/row.Total, axis=1)
app_pivot

# It looks like more people from Group B turned in an application.  Why might that be?
# 
# We need to know if this difference is statistically significant.
# Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.
# Is this result significant?

from scipy.stats import chi2_contingency
X = [[250, 2254],
     [325, 2175]]
chi2, pval, dof, expected = chi2_contingency(X)

print(pval)

# 4: Who purchases a membership?
# Of those who picked up an application, how many purchased a membership?
# Let's begin by adding a column to `df` called `is_member` which is `Member` if `purchase_date` is not `None`, and `Not Member` otherwise.

df['is_member'] = df.apply(lambda row: 'Member' if row.purchase_date is not None else 'Not Member', axis=1)
df.head()

# Now, let's create a DataFrame called `just_apps` the contains only people who picked up an application.

just_apps = df[(df.is_application == 'Application')]
just_apps.head()

# Great! Now, let's do a `groupby` to find out how many people in `just_apps` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:
# |is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|
# |-|-|-|-|-|-|
# |0|A|?|?|?|?|
# |1|B|?|?|?|?|
# 
# Save your final DataFrame as `member_pivot`.

just_ap_gp = just_apps.groupby(['ab_test_group', 'is_member']).first_name.count().reset_index()

member_pivot = just_ap_gp.pivot(index='ab_test_group',
                             columns='is_member',
                             values='first_name').reset_index()
member_pivot['Total'] = member_pivot.apply(lambda row: row.Member+row['Not Member'], axis=1)
member_pivot['Percent Purchase'] = member_pivot.apply(lambda row: row.Member/row.Total, axis=1)
member_pivot.head()

# It looks like people who took the fitness test were more likely to purchase a membership **if** they picked up an application.  Why might that be?
# Just like before, we need to know if this difference is statistically significant.  Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.
# Is this result significant?


from scipy.stats import chi2_contingency
X2 = [[200, 50],
     [250, 75]]
chi2, pval2, dof, expected = chi2_contingency(X2)

print(pval2)

# Previously, we looked at what percent of people **who picked up applications** purchased memberships.  What we really care about is what percentage of **all visitors** purchased memberships.  Return to `df` and do a `groupby` to find out how many people in `df` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:
# |is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|
# |-|-|-|-|-|-|
# |0|A|?|?|?|?|
# |1|B|?|?|?|?|
# 
# Save your final DataFrame as `final_member_pivot`.

all_vis = df.groupby(['ab_test_group', 'is_member']).first_name.count().reset_index()

final_member_pivot = all_vis.pivot(index='ab_test_group',
                             columns='is_member',
                             values='first_name').reset_index()
final_member_pivot['Total'] = final_member_pivot.apply(lambda row: row.Member+row['Not Member'], axis=1)
final_member_pivot['Percent Purchase'] = final_member_pivot.apply(lambda row: row.Member/row.Total, axis=1)
final_member_pivot

# Previously, when we only considered people who had **already picked up an application**, we saw that there was no significant difference in membership between Group A and Group B.
# 
# Now, when we consider all people who **visit MuscleHub**, we see that there might be a significant different in memberships between Group A and Group B.  Perform a significance test and check.

from scipy.stats import chi2_contingency
X3 = [[200, 2304],
     [250, 2250]]
chi2, pval3, dof, expected = chi2_contingency(X3)

print(pval3)


# 5: Summarize the acquisition funel with a chart

# We'd like to make a bar chart for Janet that shows the difference between Group A (people who were given the fitness test) and Group B (people who were not given the fitness test) at each state of the process:
# - Percent of visitors who apply
# - Percent of applicants who purchase a membership
# - Percent of visitors who purchase a membership
# Create one plot for **each** of the three sets of percentages that you calculated in `app_pivot`, `member_pivot` and `final_member_pivot`.  Each plot should:
# - Label the two bars as `Fitness Test` and `No Fitness Test`
# - Make sure that the y-axis ticks are expressed as percents (i.e., `5%`)
# - Have a title

ax1 = plt.subplot()
plt.bar(range(2), app_pivot['Percent with Application'])
ax1.set_xticks(range(2))
ax1.set_yticks([0.05, 0.10, 0.15, 0.20])
ax1.set_yticklabels(['5%', '10%', '15%', '20%'])
ax1.set_xticklabels(['Fitness Test', 'No Fitness Test'])
plt.title('Application per Visit')
plt.show()

ax2 = plt.subplot()
plt.bar(range(2), member_pivot['Percent Purchase'])
ax2.set_xticks(range(2))
ax2.set_yticks([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90])
ax2.set_yticklabels(['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'])
ax2.set_xticklabels(['Fitness Test', 'No Fitness Test'])
plt.title('Purchase / Application')
plt.show()

ax3 = plt.subplot()
plt.bar(range(2), final_member_pivot['Percent Purchase'])
ax3.set_xticks(range(2))
ax3.set_yticks([0.02, 0.04, 0.06, 0.08, 0.1])
ax3.set_yticklabels(['2%', '4%', '6%', '8%', '10%'])
ax3.set_xticklabels(['Fitness Test', 'No Fitness Test'])
plt.title('Purchase / Visit')
plt.show()

