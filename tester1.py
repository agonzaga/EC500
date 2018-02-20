from assignment1 import module

def test1():
	# Test 1 - Failures
	ret = ''
	ret += "<p> <b>Test 1: Failures </b> </p>"
	ret += ("This test will showcase the modules limitations and how it handles cases of deliberate errors")

	ret += "<p><b>Test 1.1 - Invalid username</b></p>"
	ret += "Trying username ndaksdakjdn. Result:"
	var = module('ndajsdakjdn', 10)
	ret += '<p>' + str(var) + '</p>'

	ret += "<p><b>Test 1.2 - No media content in tweets</b></p>"
	ret += "<p>Trying username neiltyson for 2 tweets. Result:</p>"
	var1 = module('neiltyson', 2)
	ret += '<p>' + str(var) + '</p>'

	return ret


if __name__ == '__main__':
	test1()