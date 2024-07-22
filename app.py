import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry
from database import Database
from add_event import AddEventPage
from view_event import ViewEventPage
from time_picker import TimePicker


class BusyApp:
    """Main application class for 'Is Cardiff Busy?'"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Is Cardiff busy?")
        self.database = Database()
        self.page_state = None
        self.busiest_event = None
        self.overall_crowd = 0
        self.amount_events = 0
        self.homepage_datetime = datetime.now()
        self.initialize_ui()
        self.update_page_state()
        self.root.mainloop()

    def initialize_ui(self):
        """Initializes the user interface components."""
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)

        # FRAMES
        self.frames = {}

        # Create and add HomePage
        home_page = HomePage(parent=container, controller=self)
        self.frames["HomePage"] = home_page
        home_page.grid(row=0, column=0, sticky="nsew")

        # Create adminPage
        admin_page = AdminArea(parent=container, controller=self)
        self.frames["AdminArea"] = admin_page
        admin_page.grid(row=0, column=0, sticky="nsew")

        # Create addEventPage
        add_event_page = AddEventPage(parent=container, controller=self)
        self.frames["AddEventPage"] = add_event_page
        add_event_page.grid(row=0, column=0, sticky="nsew")

        # Create viewEventPage
        view_event_page = ViewEventPage(parent=container, controller=self)
        self.frames["ViewEventPage"] = view_event_page
        view_event_page.grid(row=0, column=0, sticky="nsew")

        # Show the initial page
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Displays the specified frame."""
        frame = self.frames[page_name]
        frame.tkraise()

    def update_page_state(self, custom_datetime=None):
        """Updates the page state based on the current or custom datetime."""
        from busyness import is_cardiff_busy  # Import moved inside method to avoid circular import

        # use the custom datetime if provided, otherwise use the current datetime
        self.homepage_datetime = custom_datetime if custom_datetime else datetime.now()

        # call current events from the database
        current_events = self.database.get_current_events(self.homepage_datetime)
        print(f"Current events: {current_events}")  # Debug print statement

        # Call is_cardiff_busy function to get the answer and overall amount of events and crowd size
        self.page_state, self.busiest_event, self.overall_crowd, self.amount_events = is_cardiff_busy(current_events)

        print(f"Page state: {self.page_state}")  # Debug print

        # Update the UI with pagestate
        self.frames["HomePage"].update_page(self.page_state, self.busiest_event, self.overall_crowd, self.amount_events)

    def get_homepage_datetime(self):
        """Returns the datetime used for the homepage text."""
        return self.homepage_datetime

class HomePage(tk.Frame):
    """Home page frame for the application."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure the grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Page title label
        self.label = tk.Label(self, text="Is Cardiff busy?", font=("Helvetica", 24, "bold"))
        self.label.grid(row=0, column=0, pady=(5, 5))  # Adjusted padding

        # Busy label placeholder
        self.busy_label = tk.Label(self, text="YES", font=("Helvetica", 80, "bold"), bg="red")  # Reduced font size
        self.busy_label.grid(row=1, column=0, pady=(5, 5))  # Adjusted padding

        # Reasoning label
        self.reason_str = tk.StringVar()
        self.reason_str.set('Placeholder text')
        self.reasoning_label = tk.Label(self, textvariable=self.reason_str, font=("Helvetica", 14))
        self.reasoning_label.grid(row=2, column=0, pady=(5, 5))  # Adjusted padding

        # Frame for date and time input module
        input_frame = tk.Frame(self)
        input_frame.grid(row=3, column=0, pady=(5, 100))  # Added more padding below calendar widget to stop it spiling off screen

        # Entry for custom date and time (for testing and extra functionality)
        self.date_entry = DateEntry(input_frame, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=0, padx=5)

        self.time_picker = TimePicker(input_frame)
        self.time_picker.grid(row=0, column=1, padx=5)

        # Button to update the page state based on custom time inputted
        self.check_button = ttk.Button(input_frame, text="Check Date", command=self.check_busyness)
        self.check_button.grid(row=0, column=2, padx=5)

        # Admin area button placed at the top right
        self.admin_area_button = ttk.Button(self, text="Admin Area", command=lambda: controller.show_frame("AdminArea"))
        self.admin_area_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    def check_busyness(self):
        """Checks busyness based on the selected date and time."""
        try:
            # Get the date from the date entry
            selected_date = self.date_entry.get_date()
            selected_time = self.time_picker.get_time()

            # Combine the date and time into a single datetime object
            custom_datetime_str = f"{selected_date} {selected_time}"
            custom_datetime = datetime.strptime(custom_datetime_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            # Show error message if the datetime format is invalid
            messagebox.showerror("Invalid DateTime", "Please enter a valid date and time in the format YYYY-MM-DD HH:MM:SS")
            return

        # Update the page state with the processed datetime
        self.controller.update_page_state(custom_datetime=custom_datetime)

    def update_page(self, page_state, busiest_event, overall_crowd, amount_events):
        """Updates the home page based on the page state."""
        # Get the homepage datetime
        homepage_datetime = self.controller.get_homepage_datetime()
        print(f"Homepage datetime: {homepage_datetime}") #debug

        # Format the date in UK format
        date_str = homepage_datetime.strftime('%d/%m/%Y')

        # Check if the homepage datetime is the same as today's date (ignoring the specific time)
        is_today = homepage_datetime.date() == datetime.now().date()

        # Set the background colour based on the page state and change the text depending on the conditions
        color = "white"  # Default colour before any state is found
        
        if page_state == "yes":
            color = "red"
            self.busy_label.config(text="YES!")
            self.reason_str.set(f"Cardiff has {amount_events} event{'s' if amount_events != 1 else ''} {'currently' if is_today else 'on ' + date_str}\n with {overall_crowd} people attending, including a '{busiest_event.event_name}' event.")

        elif page_state == "no":
            color = "green"
            self.busy_label.config(text="NO!")
            self.reason_str.set(f"Cardiff shouldn't be busy, there {'is only' if amount_events == 1 else 'are only'} {amount_events} event{'s' if amount_events != 1 else ''} {'currently' if is_today else 'on ' + date_str}\n with {'only' if overall_crowd <= 1 else ''} {overall_crowd} people attending.")

        elif page_state == "maybe":
            color = "orange"
            self.busy_label.config(text="MAYBE?!")
            self.reason_str.set(f"Cardiff has {amount_events} event{'s' if amount_events != 1 else ''} {'currently' if is_today else 'on ' + date_str},\n with {overall_crowd} people attending, including a '{busiest_event.event_name}' event,\n so it could be busy.")

        # Apply the background colour to all relevant widgets
        self.config(bg=color)
        self.label.config(bg=color)
        self.busy_label.config(bg=color)
        self.reasoning_label.config(bg=color)


class AdminArea(tk.Frame):
    """Admin area page frame for the application."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Admin area", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

        # Add buttons to navigate to Add Event
        self.add_event_button = ttk.Button(self, text="Add Event", command=lambda: controller.show_frame("AddEventPage"))
        self.add_event_button.pack(pady=10)

        # Button to view / delete Event pages
        self.view_event_button = ttk.Button(self, text="View / Delete Events", command=lambda: controller.show_frame("ViewEventPage"))
        self.view_event_button.pack(pady=10)

        # Home page button
        self.home_page_button = ttk.Button(self, text="Home Page", command=lambda: controller.show_frame("HomePage"))
        self.home_page_button.pack(pady=10)


if __name__ == "__main__":
    app = BusyApp()
