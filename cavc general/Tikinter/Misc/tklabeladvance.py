from tkinter import *
from tkinter import ttk

# Create the window.  
root = Tk()

#  Create a Label.
label= Label(root, text =  "Hello Python")
label.config(text =  "Hello World", fg='red')
label.config(bg='yellow')
label.config(font='Arial 12')
label.config(text='Hello Tkinter, This is great GUI App')
label.config(wraplength='150')
label.config(justify=RIGHT)
label.pack()

# Define window size
root.geometry("250x300")
# Run the parent, and its children.  
root.mainloop()
