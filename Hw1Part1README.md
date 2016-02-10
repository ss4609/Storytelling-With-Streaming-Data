#HW1 Part 1
##Consuming meetup.com rsvp event stream and plotting realtime rsvp counts by state

The stream is present here at http://stream.meetup.com/2/rsvps. The detailed documentation is present at http://www.meetup.com/meetup_api/docs/stream/2/rsvps/.

Everytime some one does a rsvp on meetup.com, a json object is streamed. The data emitted contains details about the meetup event, member and meetup group.

##Volume of the messages
It varies depending on the time of the day but is generally more that 1 per minute (I have seen it upto 100 per minute as well).

##Sample JSON
NOTE: Data dictionary present at www.meetup.com/meetup_api/docs/stream/2/rsvps

{
  "venue": {
    "venue_name": "The George and Dragon",
    "lon": -1.796496,
    "lat": 51.071743,
    "venue_id": 24352961
  },
  "visibility": "public",
  "response": "yes",
  "guests": 0,
  "member": {
    "member_id": 192055375,
    "photo": "http://photos1.meetupstatic.com/photos/member/b/7/5/4/thumb_249286932.jpeg",
    "member_name": "Sheila"
  },
  "rsvp_id": 1593307836,
  "mtime": 1454871130000,
  "event": {
    "event_name": "Anti Valentines Night!!",
    "event_id": "228681164",
    "time": 1455305400000,
    "event_url": "http://www.meetup.com/Salisbury-Socialites/events/228681164/"
  },
  "group": {
    "group_topics": [
      {
        "urlkey": "socialnetwork",
        "topic_name": "Social Networking"
      },
      {
        "urlkey": "singles",
        "topic_name": "Singles"
      },
      {
        "urlkey": "nightlife",
        "topic_name": "Nightlife"
      },
      {
        "urlkey": "dating-and-relationships",
        "topic_name": "Dating and Relationships"
      },
      {
        "urlkey": "fun-times",
        "topic_name": "Fun Times"
      },
      {
        "urlkey": "newintown",
        "topic_name": "New In Town"
      },
      {
        "urlkey": "diningout",
        "topic_name": "Dining Out"
      },
      {
        "urlkey": "social",
        "topic_name": "Social"
      },
      {
        "urlkey": "graduates",
        "topic_name": "Graduates"
      },
      {
        "urlkey": "professional-singles",
        "topic_name": "Single Professionals"
      }
    ],
    "group_city": "Salisbury",
    "group_country": "gb",
    "group_id": 2066441,
    "group_name": "Salisbury Socialites",
    "group_lon": -1.8,
    "group_urlname": "Salisbury-Socialites",
    "group_lat": 51.07
  }
}

##Consumer
In the consumer I am extracting the state of the meetup for which rsvp was done and streaming that via websocketd on port 8080
The cosumer code is present at https://github.com/ss4609/Storytelling-With-Streaming-Data/blob/master/HW1Part2Consumer.py

##Visualization Webpage
The webpage, leveraging d3.js, shows the bar chart of count of rsvps by state, all getting updated realtime getting messages from websocket server that runs the consumer code. The webpage code is present at https://github.com/ss4609/Storytelling-With-Streaming-Data/blob/master/HW1Part3Index.html.

Sample screenshots present at HW1WebPageOutput1.png (https://github.com/ss4609/Storytelling-With-Streaming-Data/blob/master/media/HW1WebPageOutput1.png) and HW1WebPageOutput2.png (https://github.com/ss4609/Storytelling-With-Streaming-Data/blob/master/media/HW1WebPageOutput2.png).
Reference for d3.js code - https://bost.ocks.org/mike/bar/3/

An analysis/insight that we can gather from this application is the during business hours (common across pst and est), the highest rate of RSVP is CA followed by NY based on some spot tests done. Of course we would need to collect data over time to get a more detailed picture of the statewise RSVP trends.
