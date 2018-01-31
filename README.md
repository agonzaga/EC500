# EC500
EC500 Assigments\n

DEPENDENCIES: \n
.............from google.cloud import videointelligence\n
.............import io, os\n
.............import tweepy\n
.............import wget\n
  
  
HOW TO USE \n
 If importing into a script: -function name is module(twitter_handle, number_tweets)\n
                             -inputs are twitter name and number of tweets to analyze\n
                             -return: python dictionary with label name as key and a tuple (segment, confidence) as value.
                
