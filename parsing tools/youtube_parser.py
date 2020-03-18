from youtube_transcript_api import YouTubeTranscriptApi as YTTA
from youtube_transcript_api._errors import TranscriptsDisabled
from youtube_dl import YoutubeDL as YDL
from options import RAW_DATA_DIR, RAW_SUBT_DIR
import re
import os


def youtube_parse(url, cur):
    pat = r"((?<=(https://youtube\.com/watch\?v=))|(?<=(http://youtube\.com/watch\?v=))|(?<=(https://www\.youtube\.com/watch\?v=))|(?<=(http://www\.youtube\.com/watch\?v=)))[^\\\n&]*"
    video_id = re.search(pat, url).group(0)
    l = []

    if video_id in cur:
        return 0

    print(f"video_id = {video_id} for {url}")
    try:
        l = YTTA.get_transcript(video_id, languages=['ru', 'en'])
    except TranscriptsDisabled:
        print(f"Video {url} has no subtitles.")

    path = os.path.join(RAW_SUBT_DIR, f"{video_id}.txt")
    with open(path, 'w', encoding='utf-8') as out:
        out.write(str(l))

    return 1

def youtube_download_audio(url):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl':f'{RAW_DATA_DIR}/%(id)s.%(ext)s'
    }

    with YDL(options) as ydl:
        ydl.download([url])

def youtube_audio_trs_parse(url, cur):
    if youtube_parse(url, cur):
        youtube_download_audio(url)

def get_from_urls(path):
    l = []
    with open(path, 'r') as inp:
        lines = inp.readlines()
        for line in lines:
            l.append(line[:-1])
    return l

def cur_urls():
    files = [i[:-4] for i in os.listdir(RAW_DATA_DIR) if os.path.isfile(os.path.join(RAW_DATA_DIR,i))]
    return files

if __name__ == '__main__':
    urls = get_from_urls('urls.txt')
    curUrls = cur_urls()

    for url in urls:
        youtube_audio_trs_parse(url, curUrls)


































#
