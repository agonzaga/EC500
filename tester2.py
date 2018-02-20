from assignment1 import module
import time



# Test 2 - Timing

def test2():
	# Running module with 50 tweets
	start = time.time()
	module('neiltyson', 50)
	end = time.time()
	overall = end - start

	# Running module with 100 tweets
	start2 = time.time()
	module('neiltyson', 50)
	end2 = time.time()
	overall2 = end2 - start2

	# Printing the results
	ret = "<p> <b>Test 2: Time to run entire module with neiltyson and 50 tweets </b> </p>"
	ret += "End time: " + str(end)
	ret += "<p>Start time: " + str(start) + '</p>'
	ret += "<p>Time of execution " + str(overall) +  " seconds"


	ret += "<p> <b> Test 2.1: Time to run entire module with neiltyson and 100 tweets</b></p>"
	ret += "End time: " + str(end2)
	ret += "<p>Start time: " + str(start2) + '</p>'
	ret += "<p>Time of execution " + str(overall2) +  " seconds"

	return ret


