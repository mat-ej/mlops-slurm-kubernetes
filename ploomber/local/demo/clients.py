from ploomber.clients import S3Client

def get():
    return S3Client(bucket_name='ploomber-bucket-matej',
                    parent='hello-from-europython',
                    json_credentials_path='credentials.json')



# def get_gcloud():
#     return GCloudStorageClient(bucket_name='bucket-name',
#                                parent='ml-online',
#                                json_credentials_path='credentials.json')