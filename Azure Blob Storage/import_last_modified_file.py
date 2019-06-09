import json
from datetime import datetime

from azure.storage.blob import BlockBlobService


def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Initialize variables
    last_modified = datetime(1000, 1, 1).replace(tzinfo=None)
    local_filename = "tmp_data.xls"

    # Azure storage settings
    storage_account_name = config['AZURE_STORAGE']['STORAGE_ACCOUNT_NAME']
    secret_key = config['AZURE_STORAGE']['STORAGE_ACCOUNT_KEY']
    container_name = "data"

    # Initializing blob service connection
    blob_service = BlockBlobService(storage_account_name, secret_key)
    generator = blob_service.list_blobs(container_name)

    for blob in generator:
        modified = blob.properties.last_modified
        modified = modified.replace(tzinfo=None)
        if modified > last_modified:
            last_modified = modified
            blob_name = blob.name
    print("Last modified blob: " + blob_name + " " + str(last_modified))

    blob_service.get_blob_to_path(container_name, blob_name, local_filename)


if __name__ == "__main__":
    main()
