#Visualizing Loans Awarded by Kiva

# 1: Import Necessary Python Modules

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# 2: Ingest The Data

df = pd.read_csv('kiva_data.csv')
df.head()

print(df.head(25))


# Step 4: Bar Charts

sns.barplot(data=df, x='country', y='loan_amount')



import matplotlib.ticker as mtick

f, ax = plt.subplots(figsize=(15, 10))

sns.barplot(data=df, x="country", y = "loan_amount")

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)


# 5: Learn More By Using `hue` In Your Visualization

f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x="country", y="loan_amount")
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)


f, ax2 = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x="country", y="loan_amount", hue='gender')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax2.yaxis.set_major_formatter(tick)

# 6: Styling

sns.set_palette('Pastel2')
sns.set_style('whitegrid')
plt.figure(figsize=(25, 15))
ax.set_title("Loan amount by activity")
sns.barplot(data=df, x="country", y="loan_amount", hue='gender')


#  7: Box Plots With Kiva Data

plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x="country", y="loan_amount")
sns.set_palette('Accent')

# 8: Box Plot by Activity


plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x="activity", y="loan_amount")
sns.set_palette('Dark2')


# 9: Violin Plots

plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="activity", y="loan_amount")

plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="country", y="loan_amount")

# 10: Split Violin Plots

sns.set_palette("Spectral")
plt.figure(figsize=(18, 12))
sns.violinplot(data=df, x="country", y="loan_amount", hue='gender', split=True)






