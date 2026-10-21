# Media Downloader

A desktop app for downloading audio (MP3) or video (MP4) from YouTube and other sites supported by [yt-dlp](https://github.com/yt-dlp/yt-dlp). It has a simple Tkinter window, and it works with single videos and playlists.


## Features

- Download as MP3 or MP4
- Single videos and full playlists
- Works with any site yt-dlp supports
- Creates the download folder automatically and cleans up file names
- Skips files you have already downloaded

## Requirements

- Python 3.7 or newer
- [ffmpeg](https://ffmpeg.org/download.html), available in your system PATH
- yt-dlp (installed in the steps below)

Tkinter comes with most Python installs. On Ubuntu or Debian you may need `sudo apt install python3-tk`.

## Installation

```bash
git clone https://github.com/DevSJ06/MediaDownloder.git
cd MediaDownloder
pip install -r requirements.txt
```

## Usage

```bash
python App.py
```

Paste a video or playlist link, choose MP3 or MP4, pick a download folder and start the download.

## Project structure

```
App.py              # Tkinter GUI, run this file
downloader.py       # Download logic, built on yt-dlp
requirements.txt    # Python dependencies
LICENSE             # MIT license
```

## Disclaimer

This is a personal learning project. Only download content you have the right to download, and follow the terms of service of each site you use it with. I am not responsible for how it is used.

## License

MIT. See [LICENSE](LICENSE).
