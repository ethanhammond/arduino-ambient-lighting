import cv2
import subprocess
import numpy as np

#openCV uses bgr rather than rgb for colors
bgrWidthValues = []
bgrHeightValues = []

#reads test image from file location
# TODO: screenshot stream from display with temp images
img = cv2.imread("./arduino-ambient/test.jpg")

#declare size of image in pixels
imgDimensions = img.shape
imgWidth = imgDimensions[0]
imgHeight = imgDimensions[1]

#pixels are selected in [x,y] format, helps keep resource usage low
cmd = ['xrandr']
cmd2 = ['grep', '*']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
p.stdout.close()

resolution_str, junk = p2.communicate()
resolution = resolution_str.split()[0]
width, height = resolution.split('x')

screenWidth = width
screenHeight = height

if (screenWidth < imgWidth or screenHeight < imgHeight):
    analyzedWidth = int(screenWidth)
    analyzedHeight = int(screenHeight)
else:
    analyzedWidth = int(screenWidth)
    analyzedHeight = int(screenHeight)

#rather than analysing width*height pixels, 1/10000 are meant to be analyzed
# TODO: subject to change based on accuracy and efficiency

rows = 0
columns = 0

for rows in range(analyzedWidth):

    radius = 1
    color = [255, 255, 255]

    print(img[(rows*analyzedWidth),(columns*analyzedHeight)])
    cv2.circle(img, ((rows*analyzedWidth),(columns*analyzedHeight)), radius, color)
    rows += 1

    for columns in range(analyzedHeight):
        print(img[(rows*analyzedWidth),(columns*analyzedHeight)])
        cv2.circle(img, ((rows*analyzedWidth),(columns*analyzedHeight)), radius, color)
        columns += 1


cv2.imshow('image',img)
cv2.waitKey(0)
