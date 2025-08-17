from os import path, makedirs
import yt_dlp
from yt_dlp.utils import DownloadError
from config import DOWNLOAD_DIR  # import your safe download path (/tmp/downloads)

# make sure downloads folder exists
makedirs(DOWNLOAD_DIR, exist_ok=True)

ytdl = yt_dlp.YoutubeDL(
    {
        "outtmpl": path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s"),
        "format": "bestaudio[ext=m4a]",
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
)


def download(url: str, my_hook) -> str:
    # make sure downloads folder exists
    makedirs(DOWNLOAD_DIR, exist_ok=True)

    ydl_optssx = {
        "format": "bestaudio[ext=m4a]",
        "outtmpl": path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s"),
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
    info = ytdl.extract_info(url, False)
    try:
        x = yt_dlp.YoutubeDL(ydl_optssx)
        x.add_progress_hook(my_hook)
        dloader = x.download([url])
    except Exception as y_e:
        print(y_e)
        return None
    xyz = path.join(DOWNLOAD_DIR, f"{info['id']}.{info['ext']}")
    return xyz
