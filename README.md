##HW1 Part 1
#Consuming meetup.com rsvp event stream

The stream is present here at http://stream.meetup.com/2/rsvps. The detailed documentation is present at http://www.meetup.com/meetup_api/docs/stream/2/rsvps/.

Everytime some one does a rsvp on meetup.com, a json object is streamed. The data emitted contains details about the meetup event, member and meetup group.

#Data Dictionary
event

    Event for the RSVP

    api_version

        2
    event_id

        Unique alphanumeric identifier
    event_name

        Name of the event
    event_url

        URL to the full event page
    time

        Event time if set in milliseconds since the epoch

group

    Group hosting the event

    api_version

        2
    group_city

        Group's home city
    group_country

        two-letter code of group's home country
    group_id

        Numeric identifier of the group
    group_lat

        Latitude of group's approximate location
    group_lon

        Longitude of group's approximate location
    group_name

        -
    group_state

        two-letter code of group's home state, if in US or CA
    group_topics

        Topics associated with this group

        api_version

            2
        topic_name

            Longer name
        urlkey

            Unique keyword

    group_urlname

        Unique portion of group's URL, no slashes

guests

    Number of guests the member is bringing
member

    Member who RSVP'd

    api_version

        2
    member_id

        Unique numeric id
    member_name

        Full name given
    other_services

        e.g. {"twitter": {"identifier": "MeetupAPI"}}
    photo

        Thumbnail URL for member photo if one exists

mtime

    Last modified time of this RSVP, in milliseconds since the epoch
response

    "yes" or "no"
rsvp_id

    Unique numeric identifier
venue

    Venue, if public

    api_version

        2
    lat

        Latitude of the venue
    lon

        Longitude of the venue
    venue_id

        Unique numeric identifier
    venue_name

        -


#Sample JSON

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
