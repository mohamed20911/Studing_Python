from pytube import YouTube

link = "https://www.youtube.com/watch?v=8BCN8gXbBY8&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=36"
#link = input("Please enter the video url: ")

video = YouTube(link)

#print(f"The video title is:\n{video.title} \n--------------------------")
#print(f"The video discription is:\n{video.discription} \n--------------------------")
#print(f"The video views are: {video.views} \n--------------------------")
#print(f"The video rating is: {video.rating} \n--------------------------")
#print(f"The video duration is: {video.length/60} seconds \n--------------------------")

#print(video.streams)

#for stream in video.streams:
#    print(stream)

#for stream in video.streams.filter(progressive=True):
#    print(stream)

#for stream in video.streams.filter(progressive=True, res="720p"):
#    print(stream)

#for stream in video.streams.filter(progressive=True, res="720p", subtype="mp4"):
#    print(stream)

#print(video.streams.get_highest_resolution())

#print(video.streams.get_lowest_resolution())

def finish():
    print("Download done")
#video.streams.filter(progressive=True, res="720p", subtype="mp4", type="video").download(output_path="C:/Users/ehab/OneDrive/Desktop/YouTube videos download", filename="YouTube video downloader")
video.streams.get_highest_resolution().download(output_path="C:/Users/ehab/OneDrive/Desktop/YouTube videos download", filename="YouTube video downloader")
video.register_on_complete_callback(finish())

from pytube import Playlist

playlist_link = "https://www.youtube.com/playlist?list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ"
playlist = Playlist(link)
def finish():
    print("Download done")
for video in playlist.videos:
    video.streams.get_highest_resolution().download(output_path="C:/Users/ehab/OneDrive/Dektop/Download playlists")
