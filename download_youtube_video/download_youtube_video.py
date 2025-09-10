from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

def download_video(url: str, quality: str, output: str = "%(title)s.%(ext)s"):
    """
    使用 yt-dlp 下載 YouTube 影片。

    :param url: YouTube 影片網址
    :param quality: 畫質，例如 "best", "worst", "22", "18", "249+251"
    :param output: 輸出檔名格式（可包含 %(title)s、%(id)s、%(ext)s）
    """
    ydl_opts = {
        'format': quality,
        'outtmpl': output,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def list_formats(url):
    """
    使用 yt-dlp 列出指定 YouTube 影片的所有可用格式。
    """
    ydl_opts = {
        'listformats': True,
        'quiet': False
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    try:
        video_url = input("Enter YouTube video URL: ").strip()

        is_list_format = input("List available formats? (y/n, default is 'y'): ").strip().lower() or "y"
        if is_list_format == 'y':
            print()
            list_formats(video_url)
            print()

        quality = input("Enter desired quality (default is 'best', options: 'best', 'worst' or ID): ").strip() or "best"
        print()
        download_video(video_url, quality)
    except DownloadError as e:
        print()
