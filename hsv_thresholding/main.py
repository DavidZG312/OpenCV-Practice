import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# WindowCapture.list_window_names()
# exit()

# initialize the WindowCapture class
wincap = WindowCapture('S156-Cristala - Cristala | gamesow.com - Coowon Browser')

# item HSV filter
hsv_filter = HsvFilter(12,0,0,53,255,255,255,255,255,0)

# initialize the Vision class
vision_item = Vision('BOSS.JPG')

vision_item.init_control_gui()

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    #pre-proccess the image
    processed_image = vision_item.apply_hsv_filter(screenshot, hsv_filter)

    #do object detection
    rectangles = vision_item.find(processed_image, 0.8)
    
    #draw the detection result into the original image
    output_image = vision_item.draw_rectangles(screenshot, rectangles)

    # display the processed image
    cv.imshow('Processed', processed_image)
    cv.imshow('Matches', output_image)
    
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
