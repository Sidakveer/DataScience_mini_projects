import pandas as pd


df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)
df


df.head()
df.tail()



df.shape
df.count()

df.count()

df.groupby("TAG").sum()


df.groupby("TAG").count()

df["DATE"][1]

df.DATE[1]

type(df["DATE"][1])

type(pd.to_datetime(df.DATE[1]))

df.DATE = pd.to_datetime(df.DATE)
df.head



reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df

reshaped_df.shape

reshaped_df.columns

reshaped_df.head()

reshaped_df.count()

reshaped_df.fillna(0, inplace=True)
reshaped_df

reshaped_df.isna().values.any()


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

roll_df = reshaped_df.rolling(window=12).mean()

plt.figure(figsize=(16, 10))
plt.ylabel("Posts", fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylim(0, 35000)
for c in roll_df.columns:
    plt.plot(roll_df.index, roll_df[c], linewidth=3, label=roll_df[c].name)

plt.legend(fontsize=15)