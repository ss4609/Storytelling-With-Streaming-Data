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
