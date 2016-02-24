#Overview

In this home work, I have again chosen stream data from meetup.com which sends an event everytime some one signs up for the meetup. Details regarding the stream including the data dictionary of the stream is present in readme file of previous homework (https://github.com/ss4609/Storytelling-With-Streaming-Data/blob/master/Hw1Part1README.md).

So here I am calculating the rate of sign ups and show an alert if the signup activity goes beyond a certain threshold (configurable via command line parameter). I sever these alerts via a websocketd server on port 8080. I also created a webpage that listens to port 8080 and prints the notification. Apart from alerting when sign up activity is high, I also notify if the signup activity has returned back to normal.

#Part 1
ingestRsvpStream.py - emits the timestamps of sign ups
diff.py - emits the time difference between signups
insert.py - inserts the time differe between signups to redis (keeps for 60 s)

##run command 1 (starts the redis server)
redis-server

##run command 2 (more details and comments about this is present here https://github.com/ss4609/Storytelling-With-Streaming-Data/blob/master/HW2/registerStreamRate.sh)
python ingestRsvpStream.py | python diff.py| python insert.py


#Part 2
avg.py - calculates rate of sign up (avg time in seconds per sign up)
alert.py - generates alert if rate of sign up goes above a certain threshold

##run command

python avg.py
python alert.py .32

##part 3

run command to emit the alerts on port 8080
websocketd --port=8080 python alert.py .32

alertAction.html - web page that shows the alerts

#Sample Alerts
Alert: High activity in meetup signup!
Alert: High activity in meetup signup!
Alert: High activity in meetup signup!
Alert: Normal activity resumed in meetup sign up!

#Dependencies
Python 2.7
Non basic python packages = requests-2.9.1
Redis
Websocketd
