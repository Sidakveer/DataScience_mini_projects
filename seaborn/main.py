# -*- coding: utf-8 -*-
"""Seaborn_and_Linear_Regression_(start).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10qkOq-5yfPMr8nTeX2-h7Sc0a_KRaP7i

# Introduction

Do higher film budgets lead to more box office revenue? Let's find out if there's a relationship using the movie budgets and financial performance data that I've scraped from [the-numbers.com](https://www.the-numbers.com/movie/budgets) on **May 1st, 2018**. 

<img src=https://i.imgur.com/kq7hrEh.png>

# Import Statements
"""

import pandas as pd
import matplotlib.pyplot as plt

"""# Notebook Presentation"""

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

"""# Read the Data"""

data = pd.read_csv('cost_revenue_dirty.csv')
data

"""# Explore and Clean the Data

**Challenge**: Answer these questions about the dataset:
1. How many rows and columns does the dataset contain?
2. Are there any NaN values present?
3. Are there any duplicate rows?
4. What are the data types of the columns?
"""

data.isna().values.any()
data.duplicated().values.any()
data.info()

"""### Data Type Conversions

**Challenge**: Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format by removing `$` signs and `,`. 
<br>
<br>
Note that *domestic* in this context refers to the United States.
"""

columns = ["USD_Production_Budget", "USD_Worldwide_Gross", "USD_Domestic_Gross"]
for col in columns:
    data[col] = data[col].astype(str).str.replace("$", "")
    data[col] = data[col].astype(str).str.replace(",", "")
    data[col] = pd.to_numeric(data[col])

data.info()
data.head()

"""**Challenge**: Convert the `Release_Date` column to a Pandas Datetime type. """

data.Release_Date = pd.to_datetime(data.Release_Date)
data.info()

"""### Descriptive Statistics

**Challenge**: 

1. What is the average production budget of the films in the data set?
2. What is the average worldwide gross revenue of films?
3. What were the minimums for worldwide and domestic revenue?
4. Are the bottom 25% of films actually profitable or do they lose money?
5. What are the highest production budget and highest worldwide gross revenue of any film?
6. How much revenue did the lowest and highest budget films make?
"""

avg = data.USD_Production_Budget.mean()
avg

avg = data.USD_Production_Budget.mean()
data.describe()

"""# Investigating the Zero Revenue Films

**Challenge** How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?
"""

zero = data[data.USD_Domestic_Gross == 0]
zero.sort_values("USD_Production_Budget", ascending=False)

"""**Challenge**: How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?"""

zero = data[data.USD_Worldwide_Gross == 0]
zero.sort_values("USD_Production_Budget", ascending=False)

"""### Filtering on Multiple Conditions"""

d = data.loc[(data.USD_Domestic_Gross == 0) & (data.USD_Worldwide_Gross != 0)]
d

"""**Challenge**: Use the [`.query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) to accomplish the same thing. Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States. 

Hint: This time you'll have to use the `and` keyword.
"""

d = data.query("USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0")
d

"""### Unreleased Films

**Challenge**:
* Identify which films were not released yet as of the time of data collection (May 1st, 2018).
* How many films are included in the dataset that have not yet had a chance to be screened in the box office? 
* Create another DataFrame called data_clean that does not include these films. 
"""

# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')

unreleased = data[data.Release_Date >= scrape_date]
unreleased
clean_data = data.drop(unreleased.index)
clean_data

"""### Films that Lost Money

**Challenge**: 
What is the percentage of films where the production costs exceeded the worldwide gross revenue? 
"""

lost = clean_data.query("USD_Production_Budget > USD_Worldwide_Gross")
len(lost) * 100 / len(clean_data)

"""# Seaborn for Data Viz: Bubble Charts"""

import seaborn as sns

"""### Plotting Movie Releases over Time

**Challenge**: Try to create the following Bubble Chart:

<img src=https://i.imgur.com/8fUn9T6.png>


"""

clean_data.info()

plt.figure(figsize=(8,4), dpi=100)
 
with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=clean_data,
                        x='Release_Date', 
                        y='USD_Production_Budget',
                        hue="USD_Worldwide_Gross",
                        size='USD_Worldwide_Gross'
                        )
 
    ax.set(
        # ylim=(0, 3000000000),
          xlim=(clean_data.Release_Date.min(), clean_data.Release_Date.max()),
          xlabel='Year',
          ylabel='Budget in $100 millions'
          )

"""# Converting Years to Decades Trick

**Challenge**: Create a column in `data_clean` that has the decade of the release. 

<img src=https://i.imgur.com/0VEfagw.png width=650> 

Here's how: 
1. Create a [`DatetimeIndex` object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html) from the Release_Date column. 
2. Grab all the years from the `DatetimeIndex` object using the `.year` property.
<img src=https://i.imgur.com/5m06Ach.png width=650>
3. Use floor division `//` to convert the year data to the decades of the films.
4. Add the decades as a `Decade` column to the `data_clean` DataFrame.
"""

x = pd.DatetimeIndex(clean_data.Release_Date)
year = x.year
decade = (year  // 10 ) * 10
clean_data["Decade"] = decade
clean_data

"""### Separate the "old" (before 1969) and "New" (1970s onwards) Films

**Challenge**: Create two new DataFrames: `old_films` and `new_films`
* `old_films` should include all the films before 1969 (up to and including 1969)
* `new_films` should include all the films from 1970 onwards
* How many films were released prior to 1970?
* What was the most expensive film made prior to 1970?
"""

old_films = clean_data[clean_data.Decade < 1970]
old_films
new_films = clean_data[clean_data.Decade >= 1970]
old_films.describe()

"""# Seaborn Regression Plots"""

plt.figure(figsize=(8,4), dpi=100)
with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})

"""**Challenge**: Use Seaborn's `.regplot()` to show the scatter plot and linear regression line against the `new_films`. 
<br>
<br>
Style the chart

* Put the chart on a `'darkgrid'`.
* Set limits on the axes so that they don't show negative values.
* Label the axes on the plot "Revenue in \$ billions" and "Budget in \$ millions".
* Provide HEX colour codes for the plot and the regression line. Make the dots dark blue (#2f4b7c) and the line orange (#ff7c43).

Interpret the chart

* Do our data points for the new films align better or worse with the linear regression than for our older films?
* Roughly how much would a film with a budget of $150 million make according to the regression line?
"""

with sns.axes_style("whitegrid"):
    ax = sns.regplot(data=new_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': '#ff7c43'},
            color="#2f4b7c"
            )
    ax.set(ylim=(0, 3000000000),
         xlim=(0, 450000000),
         ylabel='Revenue in $ billions',
         xlabel='Budget in $100 millions')

"""# Run Your Own Regression with scikit-learn

$$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$
"""

from sklearn.linear_model import LinearRegression

"""**Challenge**: Run a linear regression for the `old_films`. Calculate the intercept, slope and r-squared. How much of the variance in movie revenue does the linear model explain in this case?"""

reg = LinearRegression()

from seaborn import regression
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 
reg.fit(X, y)
reg.intercept_
reg.coef_
reg.score(X, y)

"""# Use Your Model to Make a Prediction

We just estimated the slope and intercept! Remember that our Linear Model has the following form:

$$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$

**Challenge**:  How much global revenue does our model estimate for a film with a budget of $350 million? 
"""

X = pd.DataFrame(old_films, columns=["USD_Production_Budget"])
y = pd.DataFrame(old_films, columns=["USD_Worldwide_Gross"])
reg.fit(X, y)
reg.intercept_
reg.coef_
# reg.score(X, y)

pred = 22821538.63508039 + (reg.coef_[0, 0]* 350000000)
pred
# 22821538 + 1.64771314 * 350000000