from flask import Flask
from assignment1 import module
import tester1
import tester2
import tester3


app = Flask(__name__)

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<head>
   <title>API Assignment</title>
</head>
<body style="width: 880px; margin: auto;">  
    <h1>Index:</h1>
    <p>Current location <b>localhost:5000</b></p>
    <p>For API module output go to <b>/output</b></p>
    <p>For Failure Testing (Test 1) go to <b>/test1</b></p>
    <p>For Timing Testing (Test 2) go to <b>/test2</b> </p>
    <p>For Memory Testing (Test 3) go to <b>/test3<b/> </p>
    <video controls >
      <source src ="/Users/andregonzaga/Documents/Boston University/Junior/EC500/Assignment1/output.mp4" type ="video/mp4">
    </video>
</body>
"""

@app.route("/output")
def output():
    ret = module('neiltyson', 50)
    return str(ret)


@app.route("/test1")
def test1():
    ret = tester1.test1()
    return str(ret)

@app.route("/test2")
def test2():
    ret = tester2.test2()
    return str(ret)

@app.route("/test3")
def test3():
    return str(ret)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)





