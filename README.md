# EC500
EC500 Assigments<br />

DEPENDENCIES: <br />
from google.cloud import vision<br />
  import io, os<br />
  import tweepy<br />
  import wget<br />
  import glob<br />
  
  
  
HOW TO USE <br />
 If importing into a script: -function name is module(twitter_handle, number_tweets)<br />
                             -inputs are twitter name and number of tweets to analyze<br />
                             -return: python dictionary with frame number as key and list of labels as value<br />
                             
SPECIFICS: <br />
-Module will notify users through the console when incorrect/invalid information is provided. These include invalid twitter handle, failed Google authorization credentials, no images in searched tweets. 


-All images and video are saved in the current folder where script is located. Default twitter_handle is 'neiltyson' and twitter count is 100. This happens when script is run as __main__.


NOTE: As module makes use of command-line arguments such as 'rm' and 'cat', the script may not work on Windows computers.
