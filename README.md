# 🎵 Universal Media Downloader (Desktop Edition)

A Python-based application for downloading MP3 (audio) or MP4 (video) content from YouTube and other supported sites using [yt-dlp](https://github.com/yt-dlp/yt-dlp). This tool features a simple graphical interface (Tkinter) for easy downloading of single videos or playlists.

---

## 📦 Features

- ✅ Supports MP3 and MP4 formats
- ✅ Downloads from a variety of sites (YouTube, Pornhub, Facebook, TikTok, etc.)
- ✅ Playlist and single video support
- ✅ GUI built with Tkinter
- ✅ Automatic folder creation and filename sanitization
- ✅ Skips already downloaded files

---

## 🚀 Getting Started

### Requirements

- Python 3.7 or higher
- `ffmpeg` (must be in your system PATH)
- Internet connection

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/media-downloader.git
   cd media-downloader
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   python app.py
   ```

> 💡 You can also double-click the `.py` file if your system is configured with Python as the default opener.

---

## 📁 File Structure

```
media-downloader/
├── downloader.py       # Core download logic (uses yt-dlp)
├── app.py              # GUI entry point using Tkinter
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

---

## ❗ Legal Disclaimer

This tool is intended for **educational and personal use only**. Make sure you comply with the terms of service of any website you use it with. 

The developer is **not responsible** for how this software is used.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
