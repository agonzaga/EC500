import sqlite3
import assignment1

# Establish connection
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def main():
	# Creates table if first time
	create_table()

	handles = input('Please enter twitter handles separated by spaces\n')
	handles = handles.split(' ')
	number_tweets = input('Please enter number of tweets to analyze\n')

	labels = {}
	for name in handles:
		labels[name] = []
		data = assignment1.module(name, int(number_tweets))
		if type(data) == dict:
			for item in data['0']:
				labels[name].append(item)

	# Populating sqlite db
	for key, value in labels.items():
		k = key
		v = value
		for item in v:
			data_entry(k, item)
	
	# Closing db
	conn.commit()
	c.close()
	conn.close()



# Creates table if there isnt one
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS twitterData(handle TEXT, label TEXT)')

# Enter data into table
def data_entry(handle, label):
	c.execute("INSERT INTO twitterData (handle, label) VALUES (?, ?)", (handle, label))


if __name__ == '__main__':
	main()

