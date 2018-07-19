import cv2
import numpy as np
import math
from math import hypot
img=cv2.imread('cup.jpg')
maxarea=0
maxlength=0
maxwidth=0
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,140,255,cv2.THRESH_BINARY_INV)
thresh=cv2.GaussianBlur(thresh,(5,5),0)
_, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,0),2)
i=0
for c in contours:
    cnt = contours[i]
    M = cv2.moments(cnt)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect) 
    box = np.int0(box)
    points=[]
    for p in box:
        pt = (p[0],p[1])
        cx=int(p[0])
        cy=int(p[1])
        cv2.circle(img,(cx,cy),2,(0,255,0),2) 
        points.append(cx)
        points.append(cy)
    cv2.drawContours(img,[box],0,(0,0,255),2)
    width=math.sqrt( (points[0] - points[2])**2 + (points[1] - points[3])**2 )
    length=math.sqrt( (points[0] - points[6])**2 + (points[1] - points[7])**2 )
    area=length*width
    if i == 0:
        maxarea=area
        maxlength=length
        maxwidth=width
    if area>maxarea:
        maxarea=area
        maxlength=length
        maxwidth=width
    i=i+1
#print("maxlength  ", maxlength)
#print("maxwidth  ", maxwidth)      
#print("maxarea",maxarea)
Ratio=maxlength/maxwidth
#print(Ratio)
if Ratio<=2.0:
    print("          ****** Image is Of Cup ******")
if Ratio>2.0:
    print("          ****** Image is Of Pencil*****")
cv2.imshow("img",img)
cv2.waitKey(0)
