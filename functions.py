import pytube as pt
from PyQt5.QtWidgets import QFileDialog

def download_video(link,location):
    init = pt.YouTube(link)
    file = init.streams.get_highest_resolution()
    file.download(output_path=location,filename=init.title+'.mp4')
def download_audio(link,location):
    init = pt.YouTube(link)
    file = init.streams.get_audio_only()
    file.download(output_path=location,filename=init.title+'.mp3')



