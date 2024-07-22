import pyodbc
from event import Event

class Database:
    def __init__(self):
        # Connect to the database
        server = 'DELL-LAPTOP\\SQLEXPRESS'
        database = 'iscardiffbusy'
        self.connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=yes;'
        )

    def add_event(self, event):
        # Add event to database
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO event (venue_id, event_name, start, finish, event_attendance, event_url, event_type_id, event_description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (event.venue_id, event.event_name, event.start, event.finish, event.event_attendance, event.event_url, event.event_type_id, event.event_description))
        self.connection.commit()

    def get_all_events(self):
        # Get all event details
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM event ORDER BY start ASC")
        events = cursor.fetchall()
        cursor.close()
        return [Event(*event) for event in events]


    def delete_event(self, event_id):
        # Delete event by event id, this is used by view_event page
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM event WHERE event_id=?", (event_id,))
        self.connection.commit()

    def get_event_types(self):
        # Function to get all event types to help populate add event form
        cursor = self.connection.cursor()
        cursor.execute("SELECT event_type_name FROM event_type")
        event_types = [row[0] for row in cursor.fetchall()]
        return event_types
    
    def get_venues(self):
        # Gets a list of all the venues to help fill in the add event form dropdown
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM venue")
        venues = [row[0] for row in cursor.fetchall()]
        return venues
    
    def get_current_events(self, current_datetime):
        # Gets all events scheduled for the current datetime
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM event WHERE ? BETWEEN start AND finish", (current_datetime,))
        current_events = cursor.fetchall()
        print(f"Database query result: {current_events}")  # Debug print
        cursor.close()
        return [Event(*event) for event in current_events]


    def get_venue_id_by_name(self, venue_name):
        #gets venue id by name to help with adding an event to the database
        cursor = self.connection.cursor()
        cursor.execute("SELECT venue_id FROM venue WHERE name=?", (venue_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        raise ValueError(f"Venue '{venue_name}' not found")

    def get_event_type_id_by_name(self, event_type_name):
        #gets event type id by name to help with adding an event to the database
        cursor = self.connection.cursor()
        cursor.execute("SELECT event_type_id FROM event_type WHERE event_type_name=?", (event_type_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        raise ValueError(f"Event type '{event_type_name}' not found")
