set shell := ["sh", "-c"]
set windows-shell := ["powershell", "-c"]

youtube_url := "https://youtu.be/S9XNG8z0mx0"

@audio args:
	uv run main.py audio {{ args }}

metadata:
	yt-dlp --dump-json {{ youtube_url }}

artist:
   yt-dlp --print artist  {{ youtube_url }}

album:
   yt-dlp --print album  {{ youtube_url }}

album_artist:
   yt-dlp --print album_artist {{ youtube_url }}

output1:
	yt-dlp  -S "res:720,ext:mp4"  -o "%(title)s_%(uploader)s.%(ext)s" {{ youtube_url }}

test1:
	just audio {{ youtube_url }}


    
