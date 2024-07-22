import tkinter as tk
from tkinter import ttk, messagebox
from event import Event
from database import Database
from tkcalendar import DateEntry
from time_picker import TimePicker
from datetime import datetime

class AddEventPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.database = Database()

        # Title for the Add Event page
        label = ttk.Label(self, text="Add Event", font=("Arial", 18))
        label.pack(side="top", fill="x", pady=10)

        # Create input fields for event info
        self.venue_name = tk.StringVar()
        self.event_name = tk.StringVar()
        self.event_attendance = tk.StringVar()
        self.event_url = tk.StringVar()
        self.event_type_name = tk.StringVar()
        self.event_description = tk.StringVar()

        # Create labels and entries for each field
        ttk.Label(self, text="Venue:").pack(pady=5)
        self.venue_combobox = ttk.Combobox(self, textvariable=self.venue_name, values=self.database.get_venues())
        self.venue_combobox.pack(pady=5)

        ttk.Label(self, text="Event Name:").pack(pady=5)
        ttk.Entry(self, textvariable=self.event_name).pack(pady=5)

        ttk.Label(self, text="Start Date:").pack(pady=5)
        self.start_date_entry = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.start_date_entry.pack(pady=5)

        ttk.Label(self, text="Start Time:").pack(pady=5)
        self.start_time_picker = TimePicker(self)
        self.start_time_picker.pack(pady=5)

        ttk.Label(self, text="Finish Date:").pack(pady=5)
        self.finish_date_entry = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.finish_date_entry.pack(pady=5)

        ttk.Label(self, text="Finish Time:").pack(pady=5)
        self.finish_time_picker = TimePicker(self)
        self.finish_time_picker.pack(pady=5)

        ttk.Label(self, text="Event Attendance:").pack(pady=5)
        ttk.Entry(self, textvariable=self.event_attendance).pack(pady=5)

        ttk.Label(self, text="Event URL:").pack(pady=5)
        ttk.Entry(self, textvariable=self.event_url).pack(pady=5)

        ttk.Label(self, text="Event Type:").pack(pady=5)
        self.event_type_combobox = ttk.Combobox(self, textvariable=self.event_type_name, values=self.database.get_event_types())
        self.event_type_combobox.pack(pady=5)

        ttk.Label(self, text="Event Description:").pack(pady=5)
        ttk.Entry(self, textvariable=self.event_description).pack(pady=5)

        # Submit button
        submit_button = ttk.Button(self, text="Submit", command=self.submit_event)
        submit_button.pack(pady=10)

        # Admin area button placed at the top right
        self.admin_area_button = ttk.Button(self, text="Admin Area", command=lambda: controller.show_frame("AdminArea"))
        self.admin_area_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    def submit_event(self):
        try:
            # Validation checks rejects form if ther is no event name, venue or attendance
            if not self.venue_name.get() or not self.event_name.get() or not self.event_attendance.get():
                raise ValueError("Please fill in all mandatory fields.")

            # Check if attendance is a positive integer not above 150,000
            if not self.event_attendance.get().isdigit() or int(self.event_attendance.get()) <= 0 or int(self.event_attendance.get()) >= 150000:
                raise ValueError("Attendance must be a positive integer not exceeding 150,000.")

            # Get the venue id from the venue name
            venue_id = self.database.get_venue_id_by_name(self.venue_name.get())

            # Convert the event type name into the event type id
            event_type_id = self.database.get_event_type_id_by_name(self.event_type_name.get())

            # Combine date and time from DateEntry and TimePicker
            start_date = self.start_date_entry.get()
            start_time = self.start_time_picker.get_time()
            finish_date = self.finish_date_entry.get()
            finish_time = self.finish_time_picker.get_time()

            start_datetime_str = f"{start_date} {start_time}"
            start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M:%S")
            finish_datetime_str = f"{finish_date} {finish_time}"
            finish_datetime = datetime.strptime(finish_datetime_str, "%Y-%m-%d %H:%M:%S")

            # Debug print statements
            print(f"Venue ID: {venue_id}")
            print(f"Event Type ID: {event_type_id}")
            print(f"Start datetime: {start_datetime}")
            print(f"Finish datetime: {finish_datetime}")
            print(f"Event Name: {self.event_name.get()}")
            print(f"Event Attendance: {self.event_attendance.get()}")
            print(f"Event URL: {self.event_url.get()}")
            print(f"Event Description: {self.event_description.get()}")

            event = Event(
                event_id=None,
                venue_id=venue_id,
                event_name=self.event_name.get(),
                start=start_datetime,
                finish=finish_datetime,
                event_attendance=int(self.event_attendance.get()),
                event_url=self.event_url.get(),
                event_type_id=event_type_id,
                event_description=self.event_description.get()
            )

            # Try to add the event to the database
            self.database.add_event(event)
            messagebox.showinfo("Success", "Event added successfully!")

            self.clear_form()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            raise  # Ensure the ValueError is raised for the test to catch
        except Exception as e:
            print(f"Exception: {str(e)}")
            messagebox.showerror("Error", f"Failed to add event: {str(e)}")
        finally:
            print("Reached finally block")

    def clear_form(self):
        print("Clearing form")
        self.venue_name.set("")
        self.event_name.set("")
        self.start_date_entry.set_date(datetime.now())
        self.start_time_picker.hour_var.set('00')
        self.start_time_picker.minute_var.set('00')
        self.start_time_picker.second_var.set('00')
        self.finish_date_entry.set_date(datetime.now())
        self.finish_time_picker.hour_var.set('00')
        self.finish_time_picker.minute_var.set('00')
        self.finish_time_picker.second_var.set('00')
        self.event_attendance.set("")
        self.event_url.set("")
        self.event_type_name.set("")
        self.event_description.set("")
        print("Form cleared")

if __name__ == "__main__":
    root = tk.Tk()
    app = AddEventPage(root, None)
    app.pack(fill="both", expand=True)
    root.mainloop()
