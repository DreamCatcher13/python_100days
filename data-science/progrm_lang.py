import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

df.head()
df.shape
df.count()

df.groupby('TAG').sum()
df.groupby('TAG').count()

df.DATE[1]  # or df['DATE'][1]
type(df["DATE"][1])

# convert column to datetime 
df.DATE = pd.to_datetime(df['DATE'])

# reshape data frame
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS') 
# index= what do you want as rows, columns= columns of df,  values= values of cells
reshaped_df.head()
reshaped_df.shape

# replace NaN
reshaped_df.fillna(0, inplace=True)  #updating existing NaN=0
# check for any NaN
reshaped_df.isna().values.any()

# making plots
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df['java'])  # x=, y=

# multiple lines on one plot
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, 
             reshaped_df[column],
             linewidth=3, 
             label=column
    )
# or
plt.plot(reshaped_df.index, reshaped_df['java'], reshaped_df.index, reshaped_df['python'],)
#legend
plt.legend(fontsize=12)

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()