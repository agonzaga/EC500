from pymongo import MongoClient
from pprint import pprint

# Initialize Mongodb client
client = MongoClient()	# Initialize client in localhost
db = client.twitter_db

print("This is the user/study information:\n")
for t in db.information.find():
	pprint(t)

print('\n')

print("This is the data collected:\n")
for t in db['data'].find():
	pprint(t)
