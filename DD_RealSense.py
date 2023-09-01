import cv2
from realsense_depth import *

dc = DepthCamera()    

while True:
    ret, depthFrame, colorFrame = dc.get_frame()

    #Show distance for a specific point
    (height, width) = (480, 640)
    point = (320, 240)
    cv2.circle(colorFrame, point, 5, (0, 0, 255))
    distance = depthFrame[point[1], point[0]]
    cv2.putText(colorFrame, "{}mm".format(distance), (point[0], point[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    cv2.imshow("Color Frame", colorFrame)
    key = cv2.waitKey(1)
    if key == 27:
        break