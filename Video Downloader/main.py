import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        # Configuration for yt-dlp
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s', 
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
            'quiet': False
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print("Video downloaded successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() # Hides the main tkinter window

    video_url = input("Please enter a YouTube url: ")
    
    save_dir = open_file_dialog() 

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location (no folder selected)")