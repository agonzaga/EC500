
# EC500
<b>Database Project </b><br />

<b>DEPENDENCIES: </b> <br />
  from google.cloud import vision<br />
  import io, os<br />
  import tweepy<br />
  import wget<br />
  import glob<br />
  import pymongo<br />
  
  
  
<b>HOW TO USE </b><br />
Download all files in the same folder. Open <b>assignment1.py</b> and insert your google API consumer information into the code. Next, run the <b>mongodb_phase2.py</b> on the terminal console. This script will ask if you want to input user information and study information. Type 'yes' to record your API and desired study parameters into the Mongo database. Follow the terminal instructions to complete this part. Then, rerun the same script through console and type 'no' in order to bypass the information input. This will now run the program and gather the desired information. See "SPECIFICS" below for database details. 
 
 
 
<b>SPECIFICS: </b><br />
Database Format:  <br />
Name: twitter_db  <br />
Collections: information, data <br />
<br />
<b>information:</b> <br />
{keys : [consumer key, consumer secret, access token, access secret], <br />
study : [# tweets, [handle1, handle2, handle2 ...]]} <br />
<br />
<b>data:</b> <br />
{handle1 : {image#, [descriptions]}, <br />
 handle2 : {image#, [descriptions]} ... }


<b>READ DATABASE </b><br />
In order to read the database and see its contents either run mongo on your terminal or run the attached "read_db" script<br />
This script will print out the contents of both 'information' and 'data' collections.


NOTE: As module makes use of command-line arguments such as 'rm' and 'cat', the script may not work on Windows computers.

