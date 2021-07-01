#Needs updating
#Make callable as python module
#Make sure cv2 is available
#Incorporate data export script

#imports
import cv2
import os
import os.path
import sys

#set proper path for modules

#dir where images are stored
image_folder = '/home/pi/Pictures'
#name of output timelapse
#.avi = audio visual imput, not being conceited this time ;)
video_name = 'agar_timelapse.avi'

#loops throught the directory to get file names
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
##^^ THIS IS WHAT YOU WILL NEED TO MAKE SURE IS IN THE CORRECT ORDER
##YOU CAN GET THIS LIST THEN SORT IT HOW YOU WANT THEN PROCESS AFTER
##YOULL NOTICE WHEN FIRST RUN IT THAT THE ORDER IS OFF

d = {}

for i in images:
    num = i[13:-4]
    d[i] = float(num)

sorted_dic = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
sorted_list = list(sorted_dic.keys())

#getting info for formatting the images for timelapse
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

#https://www.geeksforgeeks.org/saving-a-video-using-opencv/
#Syntax: cv.VideoWriter(filename, fourcc, fps, frameSize)
#Parameters:
#	filename: Input video file
#	fourcc: 4-character code of codec used to compress the frames
#	fps: framerate of videostream
#	framesize: Height and width of frame
video = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (width,height))

#making the timelapse
for image in sorted_list:
	#this shows you the order that images are getting
	#saved into the timelape
	print(image)
	#gets image data
	frame = cv2.imread(os.path.join(image_folder, image))
	#saves to video file
	video.write(frame)

#closes everything out correctly
cv2.destroyAllWindows()
video.release()

