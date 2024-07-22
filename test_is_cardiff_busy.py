import unittest
from unittest.mock import MagicMock
import tkinter as tk
from add_event import AddEventPage

# Mock Event class
class MockEvent:
    def __init__(self, event_name, event_attendance):
        self.event_name = event_name
        self.event_attendance = event_attendance

# The function to test
def is_cardiff_busy(current_events):
    """
    Takes the current events as input and adds together the attendance to determine if Cardiff is busy.
    Returns the busiest event, the amount of events, and a yes/no/maybe string for use in conditional formatting.
    """
    # Count total crowd number
    overall_crowd = sum(event.event_attendance for event in current_events)
    
    busiest_event = None
    amount_events = 0  # Initialise amount_events
    
    if current_events:
        busiest_event = max(current_events, key=lambda event: event.event_attendance)
        print(f"Busiest event name: {busiest_event.event_name}")  # Debug print
        amount_events = len(current_events)
    
    busy_string = ''
    print(f"Total attendance: {overall_crowd}")  # Debug print
    
    if overall_crowd > 50000:
        busy_string = "yes"
    elif overall_crowd > 25000:
        busy_string = "maybe"
    else:
        busy_string = "no"

    return busy_string, busiest_event, overall_crowd, amount_events

class TestAddEventPage(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = AddEventPage(self.root, None)
        self.app.database = MagicMock()

    def tearDown(self):
        self.root.destroy()

    def test_missing_event_name(self):
        # Test with missing event name
        self.app.venue_name.set("Venue 1")
        self.app.event_name.set("")
        self.app.event_attendance.set("100")

        with self.assertRaises(ValueError) as context:
            self.app.submit_event()

        self.assertEqual(str(context.exception), "Please fill in all mandatory fields.")

    def test_invalid_attendance(self):
        # Test with attendance not a positive integer
        self.app.venue_name.set("Venue 1")
        self.app.event_name.set("Event 1")
        self.app.event_attendance.set("0")  # Invalid attendance

        with self.assertRaises(ValueError) as context:
            self.app.submit_event()

        self.assertEqual(str(context.exception), "Attendance must be a positive integer not exceeding 150,000.")

        self.app.event_attendance.set("150000")  # Test Attendance over 150,000 threshold

        with self.assertRaises(ValueError) as context:
            self.app.submit_event()

        self.assertEqual(str(context.exception), "Attendance must be a positive integer not exceeding 150,000.")

    def test_event_count(self):
        # testing the function that counts the amount of events passed to it.
        event1 = MockEvent("Event 1", 10000)
        event2 = MockEvent("Event 2", 20000)
        event3 = MockEvent("Event 3", 25000)

        busy_string, busiest_event, overall_crowd, amount_events = is_cardiff_busy([event1, event2, event3])
        
        # total events should equal 3 otherwise it will fail test.
        self.assertEqual(amount_events, 3)

if __name__ == '__main__':
    unittest.main()
