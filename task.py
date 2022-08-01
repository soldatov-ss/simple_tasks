import urllib.request
from moviepy.editor import *
import os
import hashlib

video_link = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'
your_string = 'Python Bootcamp'


def string_to_hash(string: str) -> hash:
    return hashlib.md5(string.encode())


def get_gif_file(link: str) -> str:
    urllib.request.urlretrieve(link, 'video_name.mp4')
    clip = VideoFileClip("video_name.mp4").resize(height=360)
    clip.write_gif("output.gif", fps=8, program='ffmpeg')

    return os.path.abspath("output.gif")


if __name__ == '__main__':
    # pass
    print(string_to_hash(your_string).hexdigest())
    print(get_gif_file(video_link))
