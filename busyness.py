"""
Logic for calculating if Cardiff is busy at this moment in time.
"""

from database import Database

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
