from pytube import YouTube


link = input("Enter the link: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()


ys = yt.streams.get_highest_resolution()

print("downloading...")
ys.download()
print("downloaded...")
