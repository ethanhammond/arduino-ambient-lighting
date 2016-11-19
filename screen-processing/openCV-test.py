import cv2
import subprocess
import numpy as np

#openCV uses bgr rather than rgb for colors
bgrWidthValues = []
bgrHeightValues = []

#reads test image from file location
# TODO: screenshot stream from display with temp images
img = cv2.imread("./arduino-ambient/test.jpg")

#pixels are selected in [x,y] format, helps keep resource usage low
cmd = ['xrandr']
cmd2 = ['grep', '*']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
p.stdout.close()

resolution_str, junk = p2.communicate()
resolution = resolution_str.split()[0]
width, height = resolution.split('x')

#rather than analysing width*height pixels, 1/10000 are analyzed
# TODO: subject to change based on accuracy
width = int(width)/100
height = int(height)/100

wIterations = 0
hIterations = 0

for wIterations in range(width):
    print(img[wIterations*width,hIterations*height])
    wIterations += 1
    for hIterations in range(height):
        print(img[wIterations*width,hIterations*height])
        hIterations += 1
