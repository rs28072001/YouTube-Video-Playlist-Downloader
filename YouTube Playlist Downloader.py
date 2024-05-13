from pytube import Playlist
import os,re

def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)
def download_playlist(playlist_url,playlist_name):
    try:
        playlist = Playlist(playlist_url)
        print(f"Downloading {len(playlist)} videos from the playlist...")
        for idx, video in enumerate(playlist.videos, start=1):
            stream = video.streams.get_highest_resolution()
            filename = f"{idx}.{clean_filename(video.title)}.{stream.subtype}"
            filepath = os.path.join(f'./{playlist_name}', filename)
            if os.path.exists(filepath):
                print(f"{idx}. Skipping: {video.title} (Already downloaded)")
                continue
            stream.download(output_path=f'./{playlist_name}', filename=filename)
            print(f"{idx}. Downloaded: {video.title}")
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    playlist_name = input("Enter the Folder Name of That Playlist: ")
    download_playlist(playlist_url,playlist_name)
