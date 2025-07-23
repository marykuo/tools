from yt_dlp import YoutubeDL

def download_video(url: str, quality: str = "best", output: str = "%(title)s.%(ext)s"):
    ydl_opts = {
        'format': quality,
        'outtmpl': output,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    quality = input("Enter desired quality (default is 'best', options: 'best', 'worst', '144p', '360p', etc.): ").strip() or "best"
    download_video(video_url, quality)
