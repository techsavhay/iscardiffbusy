import tkinter as tk
from tkinter import ttk

class TimePicker(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hour_var = tk.StringVar(value='00')
        self.minute_var = tk.StringVar(value='00')
        self.second_var = tk.StringVar(value='00')

        # Create spinboxes for hours, minutes, and seconds
        self.hour_spinbox = ttk.Spinbox(self, from_=0, to=23, wrap=True, textvariable=self.hour_var, width=2, format="%02.0f")
        self.hour_spinbox.grid(row=0, column=0, padx=2)

        self.hour_label = tk.Label(self, text="HH")
        self.hour_label.grid(row=0, column=1, padx=2)

        self.minute_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, textvariable=self.minute_var, width=2, format="%02.0f")
        self.minute_spinbox.grid(row=0, column=2, padx=2)

        self.minute_label = tk.Label(self, text="MM")
        self.minute_label.grid(row=0, column=3, padx=2)

        self.second_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, textvariable=self.second_var, width=2, format="%02.0f")
        self.second_spinbox.grid(row=0, column=4, padx=2)

        self.second_label = tk.Label(self, text="SS")
        self.second_label.grid(row=0, column=5, padx=2)

    def get_time(self):
        # Return the time in HH:MM:SS format
        return f"{self.hour_var.get()}:{self.minute_var.get()}:{self.second_var.get()}"
