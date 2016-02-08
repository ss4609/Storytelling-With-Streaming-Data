__author__ = 'shreyas'

#!/usr/bin/env python
import requests
import json
import time
import codecs
from sys import stdout

# this script polls the citibike API, looking for changes in the number of
# citibikes at each station

availableBikes = {}
reader = codecs.getreader("utf-8")

# get the citibike response from their API
print ("start")
r = requests.get("http://stream.meetup.com/2/rsvps", stream=True)
for raw_rsvp in r.iter_lines():
    # for each station, initialise the store if necessary
    m = json.loads(raw_rsvp.decode('utf-8'))
    if "venue" in m:
        if "member" in m:
            name = m["member"]["member_name"]
            event = m["event"]["event_name"]
            lat = m["venue"]["lat"]
            lon = m["venue"]["lon"]
            print(name)
            print(event)
            print(str(lat) +", " +str(lon))
            print()

