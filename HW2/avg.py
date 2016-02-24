#calculates rate of sign up (avg time in seconds per sign up)
#code borrowed from instructor's github
#comments are my own

import redis
import json
import time
import sys

#open connection to redis database
conn = redis.Redis()

#run forever
while 1:

    #get keys
    keys  = conn.keys()
    
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
    #prints rate for debugging
    print json.dumps({"rate":rate})
    sys.stdout.flush()
    time.sleep(0.5)
