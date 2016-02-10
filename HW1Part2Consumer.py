__author__ = 'shreyas'

#!/usr/bin/env python
import requests
import json
import time
import codecs
from sys import stdout

# this script listens to the rsvp stream from meetup.com
print ("start")
#consuming the stream from source
r = requests.get("http://stream.meetup.com/2/rsvps", stream=True)
for raw_rsvp in r.iter_lines():
    # loops over all the stream messages
    try:
        m = json.loads(raw_rsvp.decode('utf-8'))
        # Filtering for meetup group state
        if "group" in m:
            group_state = m["group"]["group_state"]

            #Write output to stdout
            print group_state
            stdout.flush()
    except:
        print "Error"
        stdout.flush()
