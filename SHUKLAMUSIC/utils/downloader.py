from os import path, makedirs
import yt_dlp
from yt_dlp.utils import DownloadError

# make sure downloads folder exists
makedirs("downloads", exist_ok=True)

ytdl = yt_dlp.YoutubeDL(
    {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "format": "bestaudio[ext=m4a]",
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
)


def download(url: str, my_hook) -> str:       
    # make sure downloads folder exists
    makedirs("downloads", exist_ok=True)

    ydl_optssx = {
        "format": "bestaudio[ext=m4a]",
        "outtmpl": "downloads/%(id)s.%(ext)s",
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
    xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
    return xyz
