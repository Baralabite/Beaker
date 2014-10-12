#!/usr/bin/python
'''
This program basically does face detection an blurs the face out
'''
print __doc__

import time
from SimpleCV import *
import beaker

beaker = beaker.Beaker()
beaker.connect(("localhost", 1997))

cam = Camera() #initialize the camera
haarcascade = HaarCascade("face")

def transmit(bb):
    x, y = findCenter(bb)
    print x,y
    if x < 130:
        beaker.moveLeftWheel(1600)
        beaker.moveRightWheel(1400)
    elif x > 170:
        beaker.moveRightWheel(1600)
        beaker.moveLeftWheel(1400)
    elif bb[2] < 10:
        beaker.moveWheels(1700)
    elif bb[2] > 200:
        beaker.moveWheels(1300)
    else:
        beaker.stopWheels()

def findCenter(bb):
    return bb[0]+bb[2]/2, bb[1]+bb[3]/2

# Loop forever
while True:
    try:
        image = cam.getImage().flipHorizontal().scale(0.5)# get image, flip it so it looks mirrored, scale to speed things up
        faces = image.findHaarFeatures(haarcascade) # load in trained face file
        if faces:
            bb = faces[-1].boundingBox()
            image = image.pixelize(10,region=(bb[0],bb[1],bb[2],bb[3]))
            print bb
            transmit(bb)            
        win = image.show() #display the image
    except:
        win.quit()
        beaker.stopWheels()
        beaker.disconnect()
        break
