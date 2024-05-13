from pytube import YouTube

def download_video(url, save_path=None):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        if save_path:
            video.download(save_path)
            print(f"Video downloaded successfully to: {save_path}")
        else:
            video.download()
            print("Video downloaded successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


while True:
    # Example usage
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
