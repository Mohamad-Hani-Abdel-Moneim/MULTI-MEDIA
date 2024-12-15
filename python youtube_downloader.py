from tkinter import *
from yt_dlp import YoutubeDL
import tkinter as tk

def high_quality():
    try:
        url= entry.get()
        ydl_opts={
            'format':'best',
            'outtmpl':'downloads%(titles)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("video has been downloaded")
    except Exception as e:
        print("Error downloading")

def low_quality():
    try:
        url= entry.get()
        ydl_opts={
            'format':'worst',
            'outtmpl':'downloads%(titles)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("video has been downloaded")
    except Exception as e:
        print("Error downloading")

def audio():
    try:
        url= entry.get()
        ydl_opts={
            'format':'bestaudio',
            'outtmpl':'downloads%(titles)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Audio has been downloaded")
    except Exception as e:
        print("Error downloading")


# Initialize the main window
window = Tk()
window.title("YouTube Video Downloader") # set name of window
window.geometry("600x300") #(x,y) 
window.resizable(False, False) #for lock big window 
window.configure(bg="#2C3E50") #background color 

# Set colors 
bg = "#2C3E50"
fg = "#ECF0F1"
button_color = "#3498DB"
button_text_color = "#FFFFFF"
entry_bg_color = "#34495E"
entry_fg_color = "#ECF0F1"
button_hover_color = "#2980B9"
button_border_color = "#1ABC9C"

Label= Label(window,text="YouTube URL", bg="#2C3E50", fg="#ECF0F1", font=("Arial", 12)) 
Label.pack(pady=10) # pack is fun take me one axis is Y to determine where the label is SHOW

# The place where you paste the url & customize it
entry = Entry(window, width=55, bg="#2C3E50", fg="#ECF0F1",insertbackground="#ECF0F1", font=("Arial", 12))  
entry.pack(pady=5) # pack is fun take me one axis is Y to determine where the entry is SHOW

# The place where the button of Hight Quality show & customize it
high = Button(window, text="High Quality", command=high_quality, bg=button_color, fg=button_text_color, font=("Arial", 12), relief="groove", borderwidth=2, highlightbackground=button_border_color, highlightthickness=2)
high.pack(pady=10)# pack is fun take me one axis is Y to determine where the button is SHOW

low = Button(window, text="Low Quality",command=low_quality, bg=button_color, fg=button_text_color, font=("Arial", 12), relief="groove", borderwidth=2, highlightbackground=button_border_color, highlightthickness=2)
low.pack(pady=10)

audio = Button(window, text="Audio",command=audio, bg=button_color, fg=button_text_color, font=("Arial", 12), relief="groove", borderwidth=2, highlightbackground=button_border_color, highlightthickness=2)
audio.pack(pady=10)

# Add a footer
footer_label = tk.Label(window, text="Developed by Mohammed Hani Abdel Monaem", bg="#2C3E50", fg="#ECF0F1", font=("Arial", 10, "italic"))
footer_label.pack(side="bottom", pady=10)

window.mainloop()