import pandas as pd

def merge_csv_files(file1, file2, output_file, join_column):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Merge the DataFrames on the specified join column
    merged_df = pd.merge(df1, df2, on=join_column)

    # Write the merged DataFrame to the specified output CSV file
    merged_df.to_csv(output_file, index=False)

if __name__ == '__main__':
    # Define the file paths
    file1 = '/app/input/task1/t1.csv'
    file2 = '/app/input/task1/t2.csv'
    output_file = '/app/input/task1/out.csv'
    join_column = 'common_id'

    # Call the function to merge the files
    merge_csv_files(file1, file2, output_file, join_column)
