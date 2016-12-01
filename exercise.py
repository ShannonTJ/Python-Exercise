#This program takes two images, one with a green background, and one that will become the new background
#The image with the green background has its background set to the other image
#Shannon TJ, Winter 2014

from SimpleGraphics import *

#Prompt user to enter image names
img1 = input("Enter the name of an image that has a green background: ")
img2 = input("Enter the name of an image you want to be the new background: ")

#Load top image that has a green background
load1 = loadImage(img1)
#Load bottom image that will be the new background
load2 = loadImage(img2)

#Compute minimum width of both images
min_width = 0

min_width1 = getWidth(load1)
min_width2 = getWidth(load2)

if min_width1 < min_width2:
  min_width = min_width1
else: 
  min_width = min_width2

#Compute minimum height of both images
min_height = 0

min_height1 = getHeight(load1)
min_height2 = getHeight(load2)

if min_height1 < min_height2:
  min_height = min_height1
else:
  min_height = min_height2

#Create new image that is minimum width x  minimum height pixels
new_img = createImage(min_width, min_height)

for x in range (0, min_width):
  for y in range (0, min_height):
    r, g, b = getPixel(load1, x, y)
    if r + 20 <  g and b + 40 < g:
      r2, g2, b2 = getPixel(load2, x, y)
      putPixel(new_img, x, y, r2, g2, b2)
    else:
      putPixel(new_img, x, y, r, g, b)

#Display new image
drawImage(new_img, 0, 0)
