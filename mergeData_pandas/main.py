# -*- coding: utf-8 -*-
"""Lego_Analysis_for_Course_(start).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6MZn6FXGWsJBDmBId0UPnChXSuEwY7a

# Introduction

Today we'll dive deep into a dataset all about LEGO. From the dataset we can ask whole bunch of interesting questions about the history of the LEGO company, their product offering, and which LEGO set ultimately rules them all:

<ul type="square">
<li>What is the most enormous LEGO set ever created and how many parts did it have?</li>

<li>How did the LEGO company start out? In which year were the first LEGO sets released and how many sets did the company sell when it first launched?</li>

<li>Which LEGO theme has the most sets? Is it one of LEGO's own themes like Ninjago or a theme they licensed liked Harry Potter or Marvel Superheroes?</li>

<li>When did the LEGO company really expand its product offering? Can we spot a change in the company strategy based on how many themes and sets did it released year-on-year?</li>

<li>Did LEGO sets grow in size and complexity over time? Do older LEGO 
sets tend to have more or fewer parts than newer sets?</li>
</ul>

**Data Source**

[Rebrickable](https://rebrickable.com/downloads/) has compiled data on all the LEGO pieces in existence. I recommend you use download the .csv files provided in this lesson.

<img src="https://i.imgur.com/49FNOHj.jpg">

# Import Statements
"""



"""# Data Exploration

**Challenge**: How many different colours does the LEGO company produce? Read the colors.csv file in the data folder and find the total number of unique colours. Try using the [.nunique() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html?highlight=nunique#pandas.DataFrame.nunique) to accomplish this.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/colors.csv")
df["name"].nunique()

df.head()

"""**Challenge**: Find the number of transparent colours where <code>is_trans == 't'</code> versus the number of opaque colours where <code>is_trans == 'f'</code>. See if you can accomplish this in two different ways."""

is_trans = df.groupby("is_trans")

is_trans.count()

df["is_trans"].value_counts()

"""### Understanding LEGO Themes vs. LEGO Sets
Walk into a LEGO store and you will see their products organised by theme. Their themes include Star Wars, Batman, Harry Potter and many more.

<img src="https://i.imgur.com/aKcwkSx.png">

A lego **set** is a particular box of LEGO or product. Therefore, a single theme typically has many different sets.

<img src="https://i.imgur.com/whB1olq.png">

The <code>sets.csv</code> data contains a list of sets over the years and the number of parts that each of these sets contained.

**Challenge**: Read the sets.csv data and take a look at the first and last couple of rows.
"""

df = pd.read_csv("data/sets.csv")
df.head()
# df.tail()



"""**Challenge**: In which year were the first LEGO sets released and what were these sets called?"""

df[df.year == 1949]

"""**Challenge**: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?"""

df[df.year == 1949]

"""**Challenge**: Find the top 5 LEGO sets with the most number of parts. """

df.sort_values("num_parts", ascending=False).head()

"""**Challenge**: Use <code>.groupby()</code> and <code>.count()</code> to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019? """

sets_by_year = df.groupby("year").count()
sets_by_year["set_num"].head()

sets_by_year["set_num"].tail()

"""**Challenge**: Show the number of LEGO releases on a line chart using Matplotlib. <br>
<br>
Note that the .csv file is from late 2020, so to plot the full calendar years, you will have to exclude some data from your chart. Can you use the slicing techniques covered in Day 21 to avoid plotting the last two years? The same syntax will work on Pandas DataFrames. 
"""

plot = plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])



"""### Aggregate Data with the Python .agg() Function

Let's work out the number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.
"""

theme_by_year = df.groupby("year").agg({"theme_id": pd.Series.nunique})


theme_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
theme_by_year.head()
# df.head()



"""**Challenge**: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021). """

plt.plot(theme_by_year.index[:-2], theme_by_year.nr_themes[:-2])
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

"""### Line Charts with Two Seperate Axes"""

ax1 = plt.gca()
ax2 = plt.twinx()
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color="g")
ax2.plot(theme_by_year.index[:-2], theme_by_year.nr_themes[:-2], color="b")
ax1.set_xlabel("Year")
ax1.set_ylabel("No. of set", color="g")
ax2.set_ylabel("No. themes", color="b")


