import pandas as pd

def merge_csv_files(input_dir, output_file):
    t1 = pd.read_csv(f"{input_dir}/t1.csv")
    t2 = pd.read_csv(f"{input_dir}/t2.csv")
    merged = pd.merge(t1, t2, on="common_id")
    merged.to_csv(output_file, index=False)

if __name__ == "__main__":
    merge_csv_files("./input/task1", "./output/out.csv")
