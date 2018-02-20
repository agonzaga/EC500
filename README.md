# EC500
<b>EC500 Assigments </b><br />

<b>DEPENDENCIES: </b> <br />
from google.cloud import vision<br />
  import io, os<br />
  import tweepy<br />
  import wget<br />
  import glob<br />
  
  
<b>HOW TO USE </b><br />
 If importing into a script: -function name is module(twitter_handle, number_tweets)<br />
                             -inputs are twitter name and number of tweets to analyze<br />
                             -return: python dictionary with frame number as key and list of labels as value<br />
                             
<b>SPECIFICS: </b><br />
-Module will notify users through the console when incorrect/invalid information is provided. These include invalid twitter handle, failed Google authorization credentials, no images in searched tweets. 


-All images and video are saved in the current folder where script is located. Default twitter_handle is 'neiltyson' and twitter count is 100. This happens when script is run as __main__.


NOTE: As module makes use of command-line arguments such as 'rm' and 'cat', the script may not work on Windows computers.



<b>TESTS - LOCAL HOMEPAGE </b>

Download and save all files in one folder. Run app.py in order to initialize the local host at localhost:5000.

Follow directions in the home page to run and view test results. For example, go to localhost:5000/output to see the output of the module and localhost:5000/test1 to see the output of test 1.
