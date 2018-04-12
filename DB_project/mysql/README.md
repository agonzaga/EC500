# EC500
<b>Database Project - SQLite version </b><br />

<b>DEPENDENCIES: </b> <br />
  import sqlite3<br />
  
  
  
<b>HOW TO USE </b><br />
Download all files in the same folder. Open <b>assignment1.py</b> and insert your google API consumer information into the code. Next, run the <b>mysql_phase2.py</b> on the terminal console. This script will ask the user for the twitter handles and number of tweets to look at. After collecting the desired study information, the program will run the API and generate results into a database. See "SPECIFICS" below for database details. 
 
 
 
<b>SPECIFICS: </b><br />
Database Format:  <br />
Name: twitter.db  <br />
Columns: handle, label <br />
<br />


<b>READ DATABASE </b><br />
In order to read the database and see its contents, download <b> sqlite browser</b>. This program provides a GUI for visualizing sqlite data.


NOTE: As module makes use of command-line arguments such as 'rm' and 'cat', the script may not work on Windows computers.

