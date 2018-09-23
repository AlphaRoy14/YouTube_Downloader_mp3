#from __future__ import unicode_literals
import youtube_dl
import os 
from sys import argv #because we are making comand line application 
#download data and config 

download_options={
        'format':'bestaudio/best',
        'outtmpl':'%(title)s.%(ext)s',
        'nocheckcertificate':True,
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
            }],
        }
#making a song directory or switching over to one
if not os.path.exists('Songs'):
    os.mkdir('Songs')
else:
    os.chdir('Songs')

#Downloding the song
with youtube_dl.YoutubeDL(download_options) as YDL:
    with open('../' + argv[1],'r') as file: #expecting the text file to be in the parent forder to Songs folder 
        for song_url in file:
            try:

                YDL.download([song_url])
           # ''' brew install livav ---> it will help strip the audio from video '''
            except:
                continue 
