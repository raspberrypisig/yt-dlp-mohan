import typer
from typing_extensions import Annotated
from trogon.typer import init_tui
import subprocess


app = typer.Typer(add_completion=False)
init_tui(app)

@app.command(help="Extract audio from youtube video")
def audio(youtube_url: Annotated[str, typer.Argument()]):
    subprocess.call(["yt-dlp", 
                     "--extract-audio", 
                     "--audio-format=mp3",
                     "-P .",
                     "-o %(title)s_%(uploader)s.%(ext)s",
                     youtube_url,])

@app.command(help="Download youtube video in 720p or lower to mp4")
def video(youtube_url: Annotated[str, typer.Argument()]):
    subprocess.call(["yt-dlp",
                     "-f", "bv+ba",
                     "-P", ".", 
                     "-S", "res:1080,ext:mp4",
                     "-o", "%(title)s_%(uploader)s.%(ext)s",
                     youtube_url,
                    ])
    #print(f"Hello {youtube_url}")
    
if __name__ == "__main__":
    app()


