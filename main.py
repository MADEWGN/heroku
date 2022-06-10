import os
os.system('ffmpeg -stream_loop -1 -re -i coder.mp4 -stream_loop -1 -re -i http://pool.anison.fm:9001/AniSonFM(320) -vcodec libx264 -pix_fmt yuvj420p -maxrate 2048k -preset ultrafast -r 12 -framerate 1 -g 50 -crf 51 -c:a aac -b:a 128k -ar 44100 -strict experimental -video_track_timescale 100 -b:v 500k -f flv  rtmp://a.rtmp.youtube.com/live2/dpm6-5uvb-rz5k-d8kx-ddvf')
