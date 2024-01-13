import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from PIL import Image, ImageTk

# Function to download the video
def download_video():
    try:
        url = entry.get()
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", f"Video '{yt.title}' downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and display a YouTube logo image
# image = Image.open("youtube_logo.png")
# photo = ImageTk.PhotoImage(image)
# label = tk.Label(root, image=photo)
# label.image = photo
# label.pack(pady=10)

# Create an entry widget to paste the YouTube URL
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create a download button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack()

# Start the GUI main loop
root.mainloop()
