#generates alert if rate of sign up goes above a certain threshold
import redis
import json
import time
import sys

#connects to redis database
conn = redis.Redis()

#initializes the rates threshold
rate_threshold = 0

#handles the case when rate is not provided by user. Defaults to .32 in that case
try:
    rate_threshold= float(sys.argv[1])
except:
    rate_threshold = .32
toggle = 0

#runs forever
while 1:
    #gets the keys
    keys = conn.keys()

    #get values for the keys. These values are the time between sign ups
    values = conn.mget(keys)

    try:
        #convert the time difference values to float as redis stores as string
        deltas = [float(v) for v in values]
    except TypeError:
        #handling any type errors
        continue

    #check for the case when there is no signup in a 60 second period
    if len(deltas):
        #calculate rate as average time between sign ups
        rate = sum(deltas)/float(len(deltas))
    else:
        rate = 0


    sys.stdout.flush()
    try:
        #check if the rate is above the threshold. Prints the alert message and waits for 10 second
        if rate <= rate_threshold:
            #prints high activity alert message
            print "Alert: High activity in meetup signup!\n"
            #set the toggle to make sure that when the high activity returns to normal then we don't print the message about high activity
            toggle = 1
            sys.stdout.flush()
            time.sleep(10)
            continue
        #check if activity is back to normal
        if rate > rate_threshold and toggle == 1:
            #print message indicating resuming or normal activity
            print "Alert: Normal activity resumed in meetup sign up!\n"
            toggle = 0
            sys.stdout.flush()
            continue
    except:
        continue

    time.sleep(0.5)
