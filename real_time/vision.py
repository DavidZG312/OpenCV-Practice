import cv2 as cv
import numpy as np
import os

class Vision:

    #properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None


    #constructor
    def _init_(self,nedle_img_path, method = cv.TM_CCOEFF_NORMED):
        self.needle_img = cv.imread(nedle_img_path, cv.IMREAD_UNCHANGED)

        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        self.method = method

def find(self, haystack_img ,threshold = 0.85, debug_mode = None):
    
    result = cv.matchTemplate(haystack_img, self.needle_img, self.method) 

    locations = np.where(result >= threshold)
    # threshold = 0.17
    # locations = np.where(result <= threshold)

    locations = list(zip(*locations[::-1]))

    # First we need to create the list of [x, y, w, h] rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
        rectangles.append(rect)

    # rectangles, weights = cv.groupRectangles(rectangles,1,0.5)

    points = []
    if len(rectangles):
        print('Found needle.')



        marker_color = (0, 255, 0)
        marker_type = cv.MARKER_CROSS
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        # Loop over all the locations and draw their rectangle
        for (x, y, w, h) in rectangles:

            #Determinate center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            #save the points
            points.append((center_x,center_y))


            if debug_mode == 'rectangles':
                # Determine the box positions
                top_left =(x, y)
                bottom_right = (x + w, y + h)
                # Draw the box
                cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points': 
                cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

    if debug_mode:
        cv.imshow('Matches', haystack_img)
        #cv.waitKey()
        #cv.imwrite('result.jpg', haystack_img)

    return points