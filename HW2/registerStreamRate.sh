# These commands are used to register the rate of stream in redis. 
# There are three utilities being called with output of each being piped to other.

# Sample output generate by python ingestRsvpStream.py is:
# {"t": 1456346579.81559}
# Here t is the key and the value represents the time stamp of a sign up event on meetup.com

# Sample output generate by python ingestRsvpStream.py | python diff.py is:
# {"t": 1456346742.201618, "delta": 0.00010895729064941406}
# Here t is the timestamp and delta represent the difference in time in seconds since the last sign up event on meetup.com

# Sample output generate by python ingestRsvpStream.py | python diff.py| python insert.py is:
# {"delta": 0.05884385108947754, "time": 1456346894.274278}
# Here delta and t are same as described previously. This program inserts key value pair of t and delta into redis database
# such that the entries are stored for 60 seconds.


python ingestRsvpStream.py | python diff.py | python insert.py
