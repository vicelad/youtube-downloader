from pytube import YouTube
from tkinter import *


def choose_folder():
    pass


def show_hidden_widgets():
    pass


# Configuring the main window
window = Tk()
window.geometry("600x300")
window.resizable(width=0, height=0)
window.title("YouTube Downloader")


# Creating 2 colums
two_colums = Frame(window)
two_colums.columnconfigure(0, weight=3)
two_colums.columnconfigure(1, weight=1)


# Creating 3 colums
three_colums = Frame(window)
three_colums.columnconfigure(0, weight=1)
three_colums.columnconfigure(1, weight=1)
three_colums.columnconfigure(2, weight=1)


# Creating widgets
user_input = Entry(two_colums)
user_input.insert(0, "Paste video URL here")
user_input.configure(state=DISABLED)
start_button = Button(two_colums, text="Analyze", command=show_hidden_widgets)
choose_quality = Combobox(three_colums, values = ['360p' , '480p' , '720p'])
two_colums.pack(fill="x", padx=20, pady=10)
three_colums.pack(fill="x", padx=20, pady=20)


# Putting our widgets into correct positions
user_input.grid(row=0, column=0, sticky=W+E)
start_button.grid(row=0, column=1, sticky=W+E)


def on_click(event):
    pass


def download_video():
    pass


window.mainloop()
