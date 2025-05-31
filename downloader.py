import os
from tqdm import tqdm
import yt_dlp


def sanitize_filename(name):
    if not name:
        return "unknown"
    return "".join(c for c in name if c.isalnum() or c in "._- ").strip()


def download_media(url, base_folder='D:/MP3Download/downloads', download_format='mp3', progress_callback=None):
    skipped_items = []

    # Generic info extractor options
    ydl_extract_opts = {
        'quiet': True,
        'extract_flat': False,
        'noplaylist': False,
        'ignoreerrors': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_extract_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        error_msg = f"⚠️ Failed to fetch media info: {e}"
        print("\n" + error_msg)
        if progress_callback:
            progress_callback(f"❌ {error_msg}")
        return

    entries = info['entries'] if 'entries' in info else [info]
    print(f"🔎 Found {len(entries)} items.\n")
    if progress_callback:
        progress_callback(f"Found {len(entries)} items.")

    for entry in tqdm(entries, desc="Downloading"):
        try:
            if entry is None:
                continue

            title = sanitize_filename(entry.get('title', 'Unknown Title'))
            site = sanitize_filename(entry.get('extractor_key', 'site'))
            playlist_title = sanitize_filename(entry.get('playlist_title')) if 'playlist_title' in entry else site
            file_ext = 'mp3' if download_format == 'mp3' else 'mp4'
            output_path = os.path.join(base_folder, playlist_title, f"{title}.{file_ext}")

            if os.path.exists(output_path):
                print(f"✅ Already downloaded: {title}")
                continue

            print(f"⬇️ Downloading: {title}")
            if progress_callback:
                progress_callback(f"⬇️ Downloading: {title}")

            if download_format == 'mp3':
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'quiet': True,
                    'outtmpl': f'{base_folder}/{playlist_title}/%(title)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'noplaylist': False,
                }
            elif download_format == 'mp4':
                ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'merge_output_format': 'mp4',
                    'quiet': True,
                    'outtmpl': f'{base_folder}/{playlist_title}/%(title)s.%(ext)s',
                    'noplaylist': False,
                }
            else:
                msg = f"❌ Unsupported format: {download_format}"
                print(msg)
                if progress_callback:
                    progress_callback(msg)
                return

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([entry['webpage_url']])

        except Exception as e:
            error_msg = f"❌ Failed: {entry.get('title', 'Unknown Title')} — {e}"
            print(error_msg)
            skipped_items.append(entry.get('title', 'Unknown Title'))

    if skipped_items:
        print("\n⚠️ Skipped items due to errors:")
        for s in skipped_items:
            print(f" - {s}")

    if progress_callback:
        progress_callback("✅ Download complete.")
