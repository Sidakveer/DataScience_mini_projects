from sys import maxsize
import pandas as pd

# pd.set_option('display.max_columns', None)
df = pd.read_csv("salaries_by_college_major.csv")
df.shape
df.columns
df.isna()
df.tail()
clean_df = df.dropna()
clean_df.tail()
maxstart = clean_df["Starting Median Salary"].idxmax()
clean_df["Undergraduate Major"].loc[maxstart]
highest_mid = clean_df["Mid-Career Median Salary"].idxmax()
clean_df["Undergraduate Major"][highest_mid]
lowest_start = clean_df["Starting Median Salary"].idxmin()
clean_df["Undergraduate Major"][lowest_start]
clean_df["Starting Median Salary"][lowest_start]
lowest_start = clean_df["Mid-Career Median Salary"].idxmin()
clean_df["Undergraduate Major"][lowest_start]
clean_df["Mid-Career Median Salary"][lowest_start]
clean_df.loc[lowest_start]
# clean_df.head()
clean_df.head()
spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
clean_df.insert(1, "Spread", spread_col)
clean_df.head()
low_risk = clean_df.sort_values("Spread")
low_risk[['Undergraduate Major', 'Spread']].head()
clean_df.head()
potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head()
low_risk[['Undergraduate Major', 'Spread']].tail()
clean_df.groupby("Group").count()
pd.options.display.float_format = "{:,.2f}".format
clean_df.groupby("Group").mean()