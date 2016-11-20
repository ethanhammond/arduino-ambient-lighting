import cv2
import subprocess
import numpy as np

#get display resolution in ubuntu to define boundaries
cmd = ['xrandr']
cmd2 = ['grep', '*']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
p.stdout.close()

resolution_str, junk = p2.communicate()
resolution = resolution_str.split()[0]
width, height = resolution.split('x')

#reads test image from file location
# TODO: screenshot stream from display with temp images
img = cv2.imread("./arduino-ambient/test.jpg")

#declare size of image in pixels
imgDimensions = img.shape
imgWidth = imgDimensions[0]
imgHeight = imgDimensions[1]

averageColorPerRow = np.average(img, axis=0)
averageColor = np.average(averageColorPerRow, axis=0)

print(averageColor)

r = int(averageColor[2])
g = int(averageColor[1])
b = int(averageColor[0])

print r,g,b
