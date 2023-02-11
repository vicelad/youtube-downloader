from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import os
from tkinter.ttk import Combobox
import time


folder_name = ""


def choose_folder():
    global folder_name  # change to folder_name = function's return
    folder_name = filedialog.askdirectory()


def show_hidden_widgets():

    url_string = user_input.get()
    url_video_object = YouTube(url_string)
    title_label = Label(two_colums, text=url_video_object.title)

    directory_button = Button(
        three_colums, text="Choose folder", command=choose_folder)
    save_button = Button(three_colums, text="Save video",
                         command=download_video)

    step_1 = Label(three_colums, text="1. Choose quality:")
    step_2 = Label(three_colums, text="2. Saving folder:")
    step_3 = Label(three_colums, text="3. Download:")
    step_1.grid(row=0, column=0, sticky=W+E)
    step_2.grid(row=0, column=1, sticky=W+E)
    step_3.grid(row=0, column=2, sticky=W+E)

    title_label.grid(sticky="W", row=1, column=0, pady=10)
    choose_quality.grid(row=2, column=0, sticky=W+E)
    directory_button.grid(row=2, column=1, sticky=W+E)
    save_button.grid(row=2, column=2, sticky=W+E)


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
choose_quality = Combobox(three_colums, values=['360p', '480p', '720p'])  # ugly, breakable
two_colums.pack(fill="x", padx=20, pady=10)
three_colums.pack(fill="x", padx=20, pady=20)


# Putting our widgets into correct positions
user_input.grid(row=0, column=0, sticky=W+E)
start_button.grid(row=0, column=1, sticky=W+E)


# Adding copyright warning
warning_message = Label(window, text="WARNING! Some YouTube videos have copyright restrictions.\nDownloading copyrighted videos without permission is a criminal act.\nYou are prohibited for any illegal use of this app.\nAlways check for video copyright and YouTube's Terms of Service.\n\nPlease don't sue me :)", foreground="red")
warning_message.place(relx=.5, y=240, anchor="center")


# Clearing user input field on click
def on_click(event):
	user_input.configure(state=NORMAL)
	user_input.delete(0, END)
	user_input.unbind('<Button-1>', on_click_id) # makes the callback only work once
on_click_id = user_input.bind('<Button-1>', on_click)


def download_video():
	url_string = user_input.get()
	url_video_object = YouTube(url_string)
	youtube_video = url_video_object.streams.get_by_resolution(choose_quality.get())
	youtube_video.download(folder_name)
	warning_message.config(text="Your video is downloaded!", foreground="green")


window.mainloop()
