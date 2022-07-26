import pandas as pd

"""## Data Exploration

**Challenge**: Read the .csv file and store it in a Pandas dataframe
"""

df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)
df

"""**Challenge**: Examine the first 5 rows and the last 5 rows of the of the dataframe"""

df.head()
df.tail()

"""**Challenge:** Check how many rows and how many columns there are. 
What are the dimensions of the dataframe?
"""

df.shape
df.count()

df.count()

"""**Challenge**: Count the number of entries in each column of the dataframe"""



"""**Challenge**: Calculate the total number of post per language.
Which Programming language has had the highest total number of posts of all time?
"""

df.groupby("TAG").sum()

"""Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.

**Challenge**: How many months of data exist per language? Which language had the fewest months with an entry? 

"""

df.groupby("TAG").count()

"""## Data Cleaning

Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"
"""

df["DATE"][1]

df.DATE[1]

type(df["DATE"][1])

type(pd.to_datetime(df.DATE[1]))

df.DATE = pd.to_datetime(df.DATE)
df.head

"""## Data Manipulation


"""

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df

"""**Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe."""

reshaped_df.shape

reshaped_df.columns

reshaped_df.head()

"""**Challenge**: Count the number of entries per programming language. Why might the number of entries be different? """

reshaped_df.count()

reshaped_df.fillna(0, inplace=True)
reshaped_df

reshaped_df.isna().values.any()



"""## Data Visualisaton with with Matplotlib

**Challenge**: Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart.
"""

import matplotlib.pyplot as plt

from pandas._libs.tslibs import timestamps
plt.plot(reshaped_df.index, reshaped_df["java"])
plt.figure(figsize=(16,10)) 
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("DATE", fontsize=14)
plt.ylabel("No. OF POSTS", fontsize=14)
plt.ylim(0, 35000)
for c in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[c], label=reshaped_df[c].name, linewidth=3)

plt.legend(fontsize=14)


"""# Smoothing out Time Series Data

Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html). 
"""

roll_df = reshaped_df.rolling(window=12).mean()

plt.figure(figsize=(16, 10))
plt.ylabel("Posts", fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylim(0, 35000)
for c in roll_df.columns:
    plt.plot(roll_df.index, roll_df[c], linewidth=3, label=roll_df[c].name)

plt.legend(fontsize=15)