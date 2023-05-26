import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
df.head() # firts 5 rows
df.tail()
df.shape  # dimension
df.columns  # name of columns

df.isna() # looking for NaN value (will return True in the cell)
clear_df = df.dropna() # new data frame without NaN rows

clear_df['Starting Median Salary'].idxmax() # index of max() in the column
clear_df['Undergraduate Major'][43]  # or ].loc[43]  or clear_df.loc[43] for entire row
clear_df.loc[clear_df['Starting Median Salary'].idxmin()]

new_column = clear_df['Mid-Career 90th Percentile Salary'].subtract(clear_df['Mid-Career 10th Percentile Salary'])
clear_df.insert(1, 'Spread', new_column) # adding new column position \ name \ column

low_risk = clear_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

clear_df.groupby('Group').count()
clear_df.groupby('Group').mean()  # averange
pd.options.display.float_format = '{:,.2f}'.format   # formatting the output


