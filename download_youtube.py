from pytube import YouTube
import sys

# Check if correct number of arguments are provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py <YouTube Video URL>")
    sys.exit(1)

# Fetch the YouTube link from command line argument
link = sys.argv[1]

# Download video
try:
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    # Corrected path with proper backslash escaping
    yd.download('Downloads')
    print("Download completed successfully.")
except Exception as e:
    print("Error:", e)

