import os
import sys

from Scripts.pywin32_testall import project_root

try:
    from data_preprocessing import load_and_merge_train_data
except ModuleNotFoundError:
    print("Error: data_preprocessing module not found.")
    print("Please check your Python path or import expression.")
    print(f"Current Python path: {sys.path}")
    sys.exit(1)


def main_pipeline():
    print("Starting main pipeline...")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root_dir = os.path.dirname(script_dir)
    data_directory = os.path.join(project_root_dir, 'data')

    print(f"Data folder path that will be used in main.py: {data_directory}")

    merged_train_df = load_and_merge_train_data(data_folder_path=data_directory)

    if merged_train_df is not None:
        print("\n--- Main Pipeline: Merged Data Sample ---")
        print(merged_train_df.head())

        # Some codes here

        print("\nMain pipeline completed successfully")
    else:
        print("\nMain pipeline cannot continue due to data didn't load.")


if __name__ == '__main__':
    main_pipeline()