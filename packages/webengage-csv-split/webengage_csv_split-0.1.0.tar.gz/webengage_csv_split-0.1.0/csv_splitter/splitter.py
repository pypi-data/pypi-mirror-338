import os
import pandas as pd
import argparse

def split_spreadsheet(file_path, num_splits):
    # Create output directory if not exists
    output_dir = "splits"
    os.makedirs(output_dir, exist_ok=True)

    # Read the file without checking data types
    file_ext = os.path.splitext(file_path)[-1].lower()
    if file_ext == ".csv":
        df = pd.read_csv(file_path, dtype=str)  # Read everything as a string to avoid issues
    elif file_ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path, dtype=str)
    else:
        print("Unsupported file format. Use CSV or Excel.")
        return

    # Get total rows and calculate rows per split
    total_rows = len(df)
    print(f"{total_rows} rows found in master file")
    rows_per_split = total_rows // num_splits  # Splitting evenly
    print(f"{rows_per_split} rows adding per splitted sheet \n")

    # Get base file name for naming splits
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Split and save
    for i in range(num_splits):
        start_idx = i * rows_per_split
        end_idx = start_idx + rows_per_split if i < num_splits - 1 else total_rows  # Last split gets remaining rows

        chunk = df.iloc[start_idx:end_idx]

        # Save each split
        split_file_name = os.path.join(output_dir, f"{base_name}-{i+1}.csv")
        chunk.to_csv(split_file_name, index=False)

        print(f"Saved: {split_file_name}")

def main():
    parser = argparse.ArgumentParser(description="Split CSV/Excel file into multiple parts.")
    parser.add_argument("--split", nargs=2, metavar=("file_path", "num_splits"), help="Split a CSV/Excel file")
    
    args = parser.parse_args()

    if args.split:
        file_path, num_splits = args.split
        split_spreadsheet(file_path, int(num_splits))
    else:
        print("Invalid command. Use: we --split <file_path> <num_splits>")

if __name__ == "__main__":
    main()
