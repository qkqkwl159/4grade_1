
import cv2
from matplotlib import pyplot as plt

def updateT(mean1, mean2):
    return (mean1 + mean2)/2

#이미지 불러오기
rgb_img = cv2.imread('./img_hw2/peppers.jpg',cv2.IMREAD_COLOR)
#plt사용을 위한 BGR -> RGB변경
rgb_img = cv2.cvtColor(rgb_img , cv2.COLOR_BGR2RGB)

#channel 분리
r,g,b = cv2.split(rgb_img)


T = [127]

ret, thres1 = cv2.threshold(r,T[0],255,cv2.THRESH_TOZERO)
ret, thres2 = cv2.threshold(r,T[0],255,cv2.THRESH_TOZERO_INV)

print(thres1.mean())
print(cv2.mean(thres1))
upT = (updateT(thres1.mean(),thres2.mean()))

T0 = T[0] - upT
print(T0)

cv2.imshow('t',thres1)
cv2.imshow('2',thres2)
cv2.waitKey()