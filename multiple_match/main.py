import cv2 as cv
import numpy as np
import os

haystack_img = cv.imread('group_rectangles/imgs/MultipleItems.PNG', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('group_rectangles/imgs/Item.PNG', cv.IMREAD_UNCHANGED)

""" import sys
np.set_printoptions(threshold=sys.maxsize) """

# result = cv.matchTemplate(haystack_img, needle_img,cv.TM_SQDIFF_NORMED) 
result = cv.matchTemplate(haystack_img, needle_img,cv.TM_CCOEFF_NORMED) 

print(result)

threshold = 0.85
locations = np.where(result >= threshold)
# threshold = 0.17
# locations = np.where(result <= threshold)
print('locations',locations)

locations = list(zip(*locations[::-1]))
print('locations',locations)

if locations:
    print('Found needle.')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    # Loop over all the locations and draw their rectangle
    for loc in locations:
        # Determine the box positions
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        # Draw the box
        cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

    cv.imshow('Matches', haystack_img)
    cv.waitKey()
    #cv.imwrite('result.jpg', haystack_img)

else:
    print('Needle not found.')
