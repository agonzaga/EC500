from pymongo import MongoClient


# Initialize Mongodb client
client = MongoClient()	# Initialize client in localhost
db = client.twitter_db

print("This is the user/study information:\n")
for t in db.information.find():
	print(t)

print('\n')

print("This is the data collected:\n")
for t in db['data'].find():
	print(t)
