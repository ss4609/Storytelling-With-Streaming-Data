#Overview

In this home work, I have again chosen stream data from meetup.com which sends an event everytime some one signs up for the meetup. Details regarding the stream including the data dictionary of the stream is present in readme file of previous homework (https://github.com/ss4609/Storytelling-With-Streaming-Data/blob/master/Hw1Part1README.md).

So in this homework I am capturing the distribution of states of meetup for which rsvps are happening. I have extended the alerting system to send out an alert (I am showing it on a webpage) when the rsvp happens for a state whose probability of rsvp is less that .1%. Again as the rate of rsvp and state distribution varies during the date and time of day, I have kept this threshold so that it can be driven by user input. The general idea can be drawn by observing the distribution barchart (histogram) - also a web page that I provide, to see what is the lower 5% of distribution looks like. Again if the entropy is high then this value could be high like 2% or when entropy is low then it could be as low as .01%. 

##Run Command
Note: all the below commands should be run on separate terminal windows

redis-server

python ingest.py | python  insertStatesAndCalcDiff.py | python insertTime.py 

python apiState.py

websocketd --port=8080 python alertUnlikelyStateRsvp.py .1

Note: below are the urls

http://127.0.0.1:5000/rate

http://127.0.0.1:5000/distribution

http://127.0.0.1:5000/entropy

http://127.0.0.1:5000/probability?state=CA

http://127.0.0.1:5000/probability?state=NY

alertUnlikelyStateRsvp.html

http://127.0.0.1:5000/distributionChart

#Sample Alerts
RSVP occurred from Unlikely state: WI (probability = 0.00604229607251) 
RSVP occurred from Unlikely state: OR (probability = 0.0275650842266) 

#Dependencies
Python 2.7
Non basic python packages = requests-2.9.1
Redis
Websocketd
