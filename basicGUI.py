import tkinter as tk
from tkinter import ttk


# learning make a window wirh tkinter

# makingt the main window
window = tk.Tk() # creates the main application window
window.title("my firts window ") # to set the title of the widow
window.geometry("1080x960") # used totset the widow title

# addind a label
label = ttk.Label(window, text="my first window ") # displays text
label.pack(pady=40) #

# adding a button
def button_clicked():
    label.config(text="click the butten")

button = ttk.Button(text="click ")
button.pack(pady=20)

# adding a entry
entry = ttk.Entry(window)
entry.pack(pady=20)

# to start the gui
window.mainloop()