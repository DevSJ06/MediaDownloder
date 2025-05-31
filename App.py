import tkinter as tk
from tkinter import messagebox
import threading
from downloader import download_media  # Make sure this is the upgraded version

def start_download():
    url = url_entry.get().strip()
    selected_format = format_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a media URL.")
        return

    # UI feedback
    set_ui_state(disabled=True)
    update_status(f"Starting download ({selected_format.upper()})...")

    def run_download():
        try:
            download_media(url, download_format=selected_format, progress_callback=update_status)
            update_status("✅ Download complete.")
            messagebox.showinfo("Success", "Download complete.")
        except Exception as e:
            update_status("❌ Error occurred.")
            messagebox.showerror("Download Error", str(e))
        finally:
            set_ui_state(disabled=False)

    threading.Thread(target=run_download).start()

def update_status(message):
    status_label.config(text=message)

def set_ui_state(disabled=True):
    state = tk.DISABLED if disabled else tk.NORMAL
    url_entry.config(state=state)
    download_button.config(state=state)
    mp3_radio.config(state=state)
    mp4_radio.config(state=state)

# GUI setup
root = tk.Tk()
root.title("Universal Media Downloader")
root.geometry("500x250")
root.resizable(False, False)

tk.Label(root, text="Enter Video/Playlist URL:", font=("Arial", 10)).pack(pady=(10, 0))
url_entry = tk.Entry(root, width=60, font=("Arial", 10))
url_entry.pack(pady=5)

# Format selection
format_var = tk.StringVar(value='mp3')
tk.Label(root, text="Select Format:", font=("Arial", 10)).pack()
format_frame = tk.Frame(root)
mp3_radio = tk.Radiobutton(format_frame, text="MP3 (Audio)", variable=format_var, value='mp3', font=("Arial", 10))
mp4_radio = tk.Radiobutton(format_frame, text="MP4 (Video)", variable=format_var, value='mp4', font=("Arial", 10))
mp3_radio.pack(side=tk.LEFT, padx=10)
mp4_radio.pack(side=tk.LEFT, padx=10)
format_frame.pack(pady=5)

download_button = tk.Button(root, text="Download", command=start_download, font=("Arial", 10))
download_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="blue", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()
