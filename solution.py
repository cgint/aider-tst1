import pandas as pd

# Read the CSV files
t1_df = pd.read_csv('./input/task1/t1.csv')
t2_df = pd.read_csv('./input/task1/t2.csv')

# Merge the DataFrames on 'common_id'
merged_df = pd.merge(t1_df, t2_df, on='common_id')

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('./out.csv', index=False)
