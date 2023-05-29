import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/colors.csv')
df['name'].nunique()  # unique values by column
# count rows by values
df.groupby('is_trans').count()
df['is_trans'].value_counts()

sets = pd.read_csv('data/sets.csv')
# lego first set year
sets['year'].idxmin()
sets.sort_values('year').head()
# all sets for that year
sets.loc[sets['year'] == 1949]
# most parts
sets.sort_values(
    'num_parts',
    ascending=False
)
# sets per year
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()
# plotting
sets_by_year = sets_by_year[:-2]
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)
plt.plot(sets_by_year.index, sets_by_year['set_num'])
# aggregate data
theme_by_year = sets.groupby('year').agg({"theme_id": pd.Series.nunique})
theme_by_year.rename(columns={'theme_id':'themes'}, inplace=True)
# plotting
theme_by_year = theme_by_year[:-2]
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Themes', fontsize=14)
plt.plot(theme_by_year.index, theme_by_year['themes'])
# two separate X-axis
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx() # copy 
ax1.plot(sets_by_year.index, sets_by_year['set_num'], color='g') # diff by colors
ax2.plot(theme_by_year.index, theme_by_year['themes'], color='b')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of sets', color='g')
ax2.set_ylabel('Number of themes', color='b')
# aggregate on averange
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
# scatter 
plt.scatter(x=parts_per_set.index[:-2], y=parts_per_set['num_parts'][:-2])
# theme + name
t = pd.read_csv('data/themes.csv')
set_theme_counts = sets['theme_id'].value_counts() # series
# converting to DataFrame
set_theme_counts = pd.DataFrame({"id":set_theme_counts.index, 'set_count': set_theme_counts.values})
# merging two data frames ON column with same name
merged_df = pd.merge(set_theme_counts, t, on='id')
# bar chart
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df['name'][:10], merged_df['set_count'][:10])
