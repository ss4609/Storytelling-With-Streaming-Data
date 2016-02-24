#emits the time difference between signups
#code borrowed from instructor's github
#comments are my own

import json
import sys

last = 0
while 1:
    #read the input from cmd line (assuming piped input)
    line = sys.stdin.readline()
    #load as a json
    d = json.loads(line)
    #handles the init case when the code accepts its first input
    if last == 0 :
        last = d["t"]
        continue
    #calculates the time difference
    delta = d["t"] - last
    #Prints the time difference
    print json.dumps({"delta":delta, "t":d["t"]})
    sys.stdout.flush()
    #updates the previous time variable
    last = d["t"]

