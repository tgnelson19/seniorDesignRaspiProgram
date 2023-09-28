import firebase_admin
from firebase_admin import db
import json

cred_obj = firebase_admin.credentials.Certificate('seniordesign-9342c-firebase-adminsdk-649ck-c9a18f8baa.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://seniordesign-9342c-default-rtdb.firebaseio.com/'})
ref = db.reference('/')

with open("entries.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
