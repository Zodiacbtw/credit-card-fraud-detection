import pandas as pd
import numpy as np
import os

def load_and_merge_train_data(data_folder_path='../data/'):
    train_transaction_filename = 'train_transaction.csv'
    train_identity_filename = 'train_identity.csv'

    train_transaction_path = os.path.join(data_folder_path, train_transaction_filename)
    train_identity_path = os.path.join(data_folder_path, train_identity_filename)

    print(f"Full path (train_transaction.csv): {os.path.abspath(train_transaction_path)}")
    print(f"Full path (trian_identity.csv): {os.path.abspath(train_identity_path)}")

    try:
        print(f"{train_transaction_filename} is loading...")
        train_transaction_df = pd.read_csv(train_transaction_path)
        print(f"{train_transaction_filename} loaded successfully. Size: {train_transaction_df.shape}")

        print(f"{train_identity_filename} is loading...")
        train_identity_df = pd.read_csv(train_identity_path)
        print(f"{train_identity_filename} loaded successfully. Size: {train_identity_df.shape}")

        print("\nDataFrames are getting merged on TransactionID...")
        train_df = pd.merge(train_transaction_df, train_identity_df, on='TransactionID', how='left')
        print("Merge completed.")
        print(f"Merged train_df size: {train_df.shape}")

        print("\n---All Columns in Merged train_df ---")
        for col_name in train_df.columns:
            print(col_name)

        return train_df

    except FileNotFoundError as e:
        print(f"\nError: File not found! Please make sure that '{data_folder_path}' file is correct.")
        print(f"Checked paths:\n {os.path.abspath(train_transaction_path)}\n"
              f"{os.path.abspath(train_identity_path)}")
        print(e)
        return None
