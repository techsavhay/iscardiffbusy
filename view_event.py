import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import Database

class ViewEventPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.database = Database()

        # Title for the View Event page
        label = tk.Label(self, text="View / Edit Events", font=("Arial", 18))
        label.pack(side="top", fill="x", pady=10)

        # Create Treeview (like a table)
        self.tree = ttk.Treeview(self, columns=("Event ID", "Event Name", "Start", "Finish", "Attendance"), show='headings')
        self.tree.heading("Event ID", text="Event ID")
        self.tree.heading("Event Name", text="Event Name")
        self.tree.heading("Start", text="Start")
        self.tree.heading("Finish", text="Finish")
        self.tree.heading("Attendance", text="Attendance")

        # Configure style for alternating row colours
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        style.map('Treeview', background=[('selected', 'blue')], foreground=[('selected', 'white')])

        self.tree.tag_configure('oddrow', background='lightblue')
        self.tree.tag_configure('evenrow', background='white')

        self.tree.pack(fill="both", expand=True)

        # Add Delete button
        delete_button = tk.Button(self, text="Delete Selected", command=self.delete_selected)
        delete_button.pack(pady=10)

        self.populate_table()

        # Admin area button placed at the top right
        self.admin_area_button = ttk.Button(self, text="Admin Area", command=lambda: controller.show_frame("AdminArea"))
        self.admin_area_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    def tkraise(self, aboveThis=None):
        self.populate_table()
        super().tkraise(aboveThis)

    def populate_table(self):
        # Clear the table first
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch data from the database and populate the table, also splits them into odd and even rows for stripey effect
        event_info = self.database.get_all_events()
        for count, event in enumerate(event_info):
            if count % 2 == 0:
                self.tree.insert("", tk.END, values=(event.event_id, event.event_name, event.start, event.finish, event.event_attendance), tags=('evenrow',))
            else:
                self.tree.insert("", tk.END, values=(event.event_id, event.event_name, event.start, event.finish, event.event_attendance), tags=('oddrow',))

    def delete_selected(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("No selection", "You need to select an event to delete.")
            return

        for selected_item in selected_items:
            item = self.tree.item(selected_item)
            event_id = item["values"][0]
            #deletes the specified item using function in database.py
            self.database.delete_event(event_id)
            #also deletes the item from the table
            self.tree.delete(selected_item)

        messagebox.showinfo("Deleted", "Selected events have been deleted.")

if __name__ == "__main__":
    # Example usage of ViewEventPage in a standalone Tkinter application
    root = tk.Tk()
    view_event_page = ViewEventPage(root, None)
    view_event_page.pack(fill="both", expand=True)
    root.mainloop()
