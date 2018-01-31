# EC500
EC500 Assigments

DEPENDENCIES:
  from google.cloud import videointelligence
  import io, os
  import tweepy
  import wget
  
  
HOW TO USE:
 If importing into a script: -function name is module(twitter_handle, number_tweets)
                             -inputs are twitter name and number of tweets to analyze
                             -return: python dictionary with label name as key and a tuple (segment, confidence) as value.
                
