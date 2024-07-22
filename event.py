"""Defines an Event as class"""

class Event:
    def __init__(self, event_id, venue_id, event_name, start, finish, event_attendance, event_url, event_type_id, event_description):
        self.event_id = event_id
        self.venue_id = venue_id
        self.event_name = event_name
        self.start = start
        self.finish = finish
        self.event_attendance = event_attendance
        self.event_url = event_url
        self.event_type_id = event_type_id
        self.event_description = event_description