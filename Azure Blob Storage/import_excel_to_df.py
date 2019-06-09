import json
from azure.storage.blob import BlockBlobService
import pandas as pd

def main():

    with open('config.json', 'r') as f:
        config = json.load(f)

    # Azure storage settings
    storage_account_name = config['AZURE_STORAGE']['STORAGE_ACCOUNT_NAME']
    secret_key = config['AZURE_STORAGE']['STORAGE_ACCOUNT_KEY']
    container_name="data"
    blob_name="Stock Status by DC - 13 Months Sales (15).xls"

    # Download excel file from blob to local temporary file
    local_filename = "tmp_data.xls"
    blob_service =BlockBlobService(account_name=storage_account_name, account_key=secret_key)
    blob_service.get_blob_to_path(container_name=container_name, blob_name=blob_name, file_path=local_filename)

    # Import excel file in pandas dataframe
    df = pd.read_excel(local_filename)
    df.head()

if __name__ == "__main__":
    main()