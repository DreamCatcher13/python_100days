import pandas as pd
import plotly.express as px

pd.options.display.float_format = '{:,.2f}'.format
df_apps = pd.read_csv('apps.csv')

df_apps.sample(5) # 5 random rows
df_apps.drop(columns=['Last_Updated', 'Android_Ver'], inplace=True)  # remove column

nan_rows = df_apps[df_apps['Rating'].isna()]
print(nan_rows.shape)
df_apps_clean = df_apps.dropna()

duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]  # duplicates
print(duplicated_rows.shape)
duplicated_rows.head()
df_apps_clean[df_apps_clean['App'] == 'Instagram']
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])

df_apps_clean.sort_values(by=['Rating'], ascending=False).head(10) # getting top 10
df_apps_clean.sort_values(by=['Size_MBs'], ascending=False).head(10)
top50 = df_apps_clean.sort_values(by=['Reviews'], ascending=False).head(1000)
top50[top50['Type'] == 'Paid']

content_rating = df_apps_clean['Content_Rating'].value_counts()
# piechart
fig = px.pie(labels=content_rating.index,
    values=content_rating.values,
    title="Content Rating",
    names=content_rating.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

df_apps_clean.info()
# string replace
df_apps_clean['Installs'] = df_apps_clean['Installs'].astype(str).str.replace(',', "")
df_apps_clean['Installs'] = pd.to_numeric(df_apps_clean['Installs'])
df_apps_clean[['App', 'Installs']].groupby('Installs').count()

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
 
df_apps_clean.sort_values('Price', ascending=False).head(20)
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)

df_apps_clean['Revenue_Estimate'] = df_apps_clean['Installs'].mul(df_apps_clean['Price']) # new column
df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]

# bar chart
top10_category = df_apps_clean.Category.value_counts()[:10]
bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()