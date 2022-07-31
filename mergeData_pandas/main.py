

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/colors.csv")
df["name"].nunique()

df.head()


is_trans = df.groupby("is_trans")

is_trans.count()

df["is_trans"].value_counts()

df = pd.read_csv("data/sets.csv")
df.head()
# df.tail()



df[df.year == 1949]

df[df.year == 1949]

df.sort_values("num_parts", ascending=False).head()

sets_by_year = df.groupby("year").count()
sets_by_year["set_num"].head()

sets_by_year["set_num"].tail()


plot = plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])



theme_by_year = df.groupby("year").agg({"theme_id": pd.Series.nunique})


theme_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
theme_by_year.head()
# df.head()




plt.plot(theme_by_year.index[:-2], theme_by_year.nr_themes[:-2])
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])


ax1 = plt.gca()
ax2 = plt.twinx()
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color="g")
ax2.plot(theme_by_year.index[:-2], theme_by_year.nr_themes[:-2], color="b")
ax1.set_xlabel("Year")
ax1.set_ylabel("No. of set", color="g")
ax2.set_ylabel("No. themes", color="b")



"""**Challenge**: Use the <code>.groupby()</code> and <code>.agg()</code> function together to figure out the average number of parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?"""

parts_per_head = df.groupby("year").agg({"num_parts": pd.Series.mean})
parts_per_head.head()



"""### Scatter Plots in Matplotlib

**Challenge**: Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the average number of parts over time using a Matplotlib scatter plot. See if you can use the [scatter plot documentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html) before I show you the solution. Do you spot a trend in the chart?
"""

plt.scatter(parts_per_head.index[:-2], parts_per_head.num_parts[:-2])

"""### Number of Sets per LEGO Theme

LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the largest number of individual sets?
"""

df.head()

sets_theme_count = df.theme_id.value_counts()
sets_theme_count[:5]

themes_df = pd.read_csv("data/themes.csv")
themes_df[themes_df.name == "Star Wars"]

df[df.theme_id == 209]

sets_theme_count = df.theme_id.value_counts()
sets_theme_count[:5]
sets_theme_count = pd.DataFrame({
    "id": sets_theme_count.index,
    "set_count": sets_theme_count.values
})
sets_theme_count.head()

merged_df = pd.merge(sets_theme_count, themes_df, on="id")
merged_df.head()

plt.bar(merged_df.name[:10], merged_df.set_count[:10])

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel("Theme Name", fontsize=14, color="g")
plt.ylabel("No. of Sets", fontsize=14, color="g")

plt.bar(merged_df.name[:10], merged_df.set_count[:10])