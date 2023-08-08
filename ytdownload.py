from pytube import YouTube

link = 'https://www.youtube.com/watch?v=PAfG8P1cgiI'

yt = YouTube(link)
#print(yt.title) #prints the title

# videos = yt.streams.filter(only_audio = True) #shows only audio formats
videos = yt.streams.all() #shows all downloadable format
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
stream = int(input('enter: '))
videos[stream].download()
print('downloaded succesfully')

# ****** to download a playlist********

#from pytube import Playlist
#py = Playlist('paste the url here')
#print(f'downloading: {py.title}')
#for video in py.videos:
    #video.streams.first().download
