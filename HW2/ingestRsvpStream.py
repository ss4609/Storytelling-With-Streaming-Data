__author__ = 'shreyas'

# Emits the timestamps of sign ups
#!/usr/bin/env python
import requests
import json
import time
from sys import stdout

# this script listens to the rsvp stream from meetup.com
#consuming the stream from source
r = requests.get("http://stream.meetup.com/2/rsvps", stream=True)
#stays on forever unless the stream stops
for raw_rsvp in r.iter_lines():
    # loops over all the stream messages
    try:
        # Prints timestamp of sign up event
        print json.dumps({"t": time.time()})
        stdout.flush()

    except:
        #prevents code from breaking in case of any error
        print "Error"
        stdout.flush()
