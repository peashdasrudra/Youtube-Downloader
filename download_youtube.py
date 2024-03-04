from pytube import YouTube
import sys

if len(sys.argv) != 2:
    
    print("Please Enter The Youtube Video Link -> Usage: py download_youtube.py <YouTube Video URL>")
    sys.exit(1)


link = sys.argv[1]


try:
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    yd = yt.streams.get_highest_resolution()

    # Ensure The Corrected path with proper backslash escaping
    yd.download('Downloads')
    print("Download completed successfully!")

except Exception as e:
    print("Error:", e)

