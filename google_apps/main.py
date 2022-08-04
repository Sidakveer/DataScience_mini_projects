# -*- coding: utf-8 -*-
"""Google Play Store App Analytics (start).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FeeIwn5srags7R9L0zimMgEH81rdOQdj

# Introduction

In this notebook, we will do a comprehensive analysis of the Android app market by comparing thousands of apps in the Google Play store.

# About the Dataset of Google Play Store Apps & Reviews

**Data Source:** <br>
App and review data was scraped from the Google Play Store by Lavanya Gupta in 2018. Original files listed [here](
https://www.kaggle.com/lava18/google-play-store-apps).

# Import Statements
"""

import pandas as pd
import plotly.express as px

"""# Notebook Presentation"""

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

"""# Read the Dataset"""

df_apps = pd.read_csv('apps.csv')

"""# Data Cleaning

**Challenge**: How many rows and columns does `df_apps` have? What are the column names? Look at a random sample of 5 different rows with [.sample()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html).
"""

df_apps.describe()
# df_apps.shape
df_apps.head()

df_apps.sample(5)



"""### Drop Unused Columns

**Challenge**: Remove the columns called `Last_Updated` and `Android_Version` from the DataFrame. We will not use these columns. 
"""

df_apps.drop(columns=["Last_Updated", "Android_Ver"], inplace=True)
df_apps.head()

"""### Find and Remove NaN values in Ratings

**Challenge**: How may rows have a NaN value (not-a-number) in the Ratings column? Create DataFrame called `df_apps_clean` that does not include these rows. 
"""

nan_rows = df_apps[df_apps.Rating.isna()]
nan_rows.shape

df_apps_clean = df_apps.dropna()
df_apps_clean.shape

"""### Find and Remove Duplicates

**Challenge**: Are there any duplicates in data? Check for duplicates using the [.duplicated()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) function. How many entries can you find for the "Instagram" app? Use [.drop_duplicates()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) to remove any duplicates from `df_apps_clean`. 

"""

dup = df_apps_clean[df_apps_clean.duplicated()]
df_apps_clean[df_apps_clean.App == "Instagram"]

df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"], inplace=True)
df_apps_clean.shape







"""# Find Highest Rated Apps

**Challenge**: Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
"""

df_apps_clean.sort_values("Reviews", ascending=False).head(50)

"""# Find 5 Largest Apps in terms of Size (MBs)

**Challenge**: What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data, do you think there could be limit in place or can developers make apps as large as they please? 
"""



"""# Find the 5 App with Most Reviews

**Challenge**: Which apps have the highest number of reviews? Are there any paid apps among the top 50?
"""



"""# Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings"""

ratings = df_apps_clean.Content_Rating.value_counts()
ratings

df_apps_clean.head()

fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
hole=0.6,
)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
 
fig.show()



"""# Numeric Type Conversion: Examine the Number of Installs

**Challenge**: How many apps had over 1 billion (that's right - BILLION) installations? How many apps just had a single install? 

Check the datatype of the Installs column.

Count the number of apps at each level of installations. 

Convert the number of installations (the Installs column) to a numeric data type. Hint: this is a 2-step process. You'll have make sure you remove non-numeric characters first. 
"""

df_apps_clean.sample(3)

df_apps_clean.Installs.describe()

df_apps_clean[["App", "Installs"]].groupby("Installs").count()

df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(",", "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[["App", "Installs"]].groupby("Installs").count()
df_apps_clean.head(50)

"""# Find the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales Revenue Estimate

Let's examine the Price column more closely.

**Challenge**: Convert the price column to numeric data. Then investigate the top 20 most expensive apps in the dataset.

Remove all apps that cost more than $250 from the `df_apps_clean` DataFrame.

Add a column called 'Revenue_Estimate' to the DataFrame. This column should hold the price of the app times the number of installs. What are the top 10 highest grossing paid apps according to this estimate? Out of the top 10 highest grossing paid apps, how many are games?

"""

df_apps_clean.Price.describe()
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace("$", "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
df_apps_clean[["App", "Price"]].groupby("Price").count().tail(20)
df_apps_clean.sort_values("Price", ascending=False).head(20)

"""### The most expensive apps sub $250"""





