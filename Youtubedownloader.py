# from pytube import YouTube


# link = "https://www.youtube.com/watch?v=z53hxSGiL1A"

# youtube_1=YouTube(link)

# videos=youtube_1.streams.filter(only_audio=True)###audio
# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)
# # videos= youtube_1.streams.all()##video
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)

# strm=int(input("enter:"))

# videos[strm].download()
# print("Successfully")

###########################playlist###########################################

# from pytube import Playlist

# py=Playlist("")

# print(f"Downloading:{py.title}")

# for videos in py.videos:
#     videos.streams.first().download()