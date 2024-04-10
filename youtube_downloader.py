import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox

def select_download_location():
    download_path = filedialog.askdirectory()
    download_path_entry.delete(0, tk.END)
    download_path_entry.insert(0, download_path)

def download_video():
    try:
        yt = YouTube(url_entry.get())
        stream = yt.streams.get_highest_resolution()
        download_path = download_path_entry.get()
        stream.download(download_path)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading video: {e}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create URL entry field
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, sticky="w")
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Create download location entry field
download_path_label = tk.Label(root, text="Select Download Location:")
download_path_label.grid(row=1, column=0, sticky="w")
download_path_entry = tk.Entry(root, width=50)
download_path_entry.grid(row=1, column=1, padx=5, pady=5)
download_path_button = tk.Button(root, text="Browse", command=select_download_location)
download_path_button.grid(row=1, column=2, padx=5, pady=5)

# Create download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
