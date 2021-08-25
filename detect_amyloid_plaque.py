import numpy as np
import cv2
import sys
sys.setrecursionlimit(10000)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

img = cv2.imread('./img/eye_original.png') #파일명
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canvas = np.zeros(shape=img.shape, dtype=np.uint8)
detection_height_arr = []
detection_width_arr = []
cnt_255 = []
# canvas.fill(255)
# 200um 가 픽셀값이 175~211에 속해서 같이 나타남.
# 이거는 gray scale 조정할때 RGB 값의 가중치를 두어서 특정픽셀의 값만 추출가능 해보임.
for color_ in range(175,211):
    canvas[np.where(img == [color_])] = [255]

height , width = canvas.shape

def dfs(hei_,wid_):
    global cnt
    canvas[hei_][wid_] = 0
    cnt += 1
    for i in range(4):
        hei = hei_ + dx[i]
        wid = wid_ + dy[i]
        if hei < 0 or wid < 0 or hei >= height or wid >= width:
            continue
        if canvas[hei][wid] == 255:
            dfs(hei,wid)

for i in range(height):
    for j in range(width):
        if canvas[i][j] == 255:
            cnt = 0
            dfs(i,j)
            if 0 < cnt < 10:
                # 크기가 0이상 10이하인 픽셀의 위치값 받아오기 10이하인이유: 이미지 잡음을 줄이기위해서
                # 커다란 거면 pixel 개수가 뭉쳐있을 확률이 높음
                print(f'아밀로이드 플라크 검출 위치 height : {i} width : {j}')
                detection_height_arr.append(i)
                detection_width_arr.append(j)
            cnt_255.append(cnt)


print(f'아밀로이드 플라크 크기 : {cnt_255}')
# 아밀로이드 플라크 크기
# print(f'잡음제거 전 아밀로이드 플라크 개수 : {len(cnt_255)}')
# 아밀로이드 플라크 개수

img = cv2.imread('./img/eye_original.png')
# img = np.zeros(shape=img.shape, dtype=np.uint8)

for i in range(len(detection_height_arr)):
    img = cv2.circle(img, (detection_width_arr[i],detection_height_arr[i]), 4, (255,255,255), 1)
print(f'아밀로이드 플라크 개수 : {len(detection_height_arr)}')
cv2.imshow('amyloiad detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('eye_final_2.png', canvas)
# 이미지 저장하려면 이거 할 것.