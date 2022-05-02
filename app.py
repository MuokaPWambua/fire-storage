from firebase_admin import credentials, initialize_app, storage
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
# Init firebase with your credentials

cred = credentials.Certificate(os.path.join(current_dir, "secret.json"))
initialize_app(cred, {'storageBucket': 'bucket-url'})

# Put your local file path 

fileName = os.path.join(current_dir, "image.jpeg")
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL

blob.make_public()

print("your file url", blob.public_url)

