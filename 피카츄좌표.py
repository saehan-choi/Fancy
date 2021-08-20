import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


import sys
np.set_printoptions(threshold=sys.maxsize)  # 배열 전체를 뽑게해주는 함수
# sys.stdout = open('output.txt','w')

img = cv2.imread('a.png')
img = cv2.resize(img, dsize=(200,200), interpolation=cv2.INTER_AREA)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
con_img = cv2.drawContours(img,contours,-1,(0,255,0),3)
plt.imshow(con_img[:,:,::-1])

contours_xy = np.array(contours)

x = list()
y = list()

i = 0
z = 0

for z in range(len(((contours_xy[:][:])[:])[:])):    # array 개수
    for i in range(len(contours_xy[z])):             # 해당 행렬의 개수
        x_value = ((contours_xy[z][i])[0])[0]
        x.append(x_value)
        y_value = ((contours_xy[z][i])[0])[1]
        y.append(y_value)
        i = i+1
    z = z+1


plt.scatter(x,y)