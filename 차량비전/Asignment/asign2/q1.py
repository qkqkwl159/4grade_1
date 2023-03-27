import cv2
from matplotlib import pyplot as plt


rgb_img = cv2.imread('./img_hw2/peppers.jpg',cv2.IMREAD_COLOR)
b_plane, g_plane, r_plane = cv2.split(rgb_img)


# 슬라이싱 이용하여 RGB 색 평면 분할
b_plane = rgb_img[:, :, 0]
g_plane = rgb_img[:, :, 1]
r_plane = rgb_img[:, :, 2]
cv2.imshow('rgb',rgb_img)
cv2.imshow('B_plane', b_plane)
cv2.imshow('G_plane', g_plane)
cv2.imshow('R_plane', r_plane)
cv2.waitKey()
rgb_img = cv2.cvtColor(rgb_img , cv2.COLOR_BGR2RGB)

r,g,b = cv2.split(rgb_img)
m = cv2.merge((r,g,b))

plt.subplot(3,3,1)
plt.imshow(rgb_img)
plt.axis('off')

plt.subplot(3,3,4)
plt.imshow(r,cmap='gray')
plt.axis('off')

plt.subplot(3,3,5)
plt.imshow(g, cmap='gray')
plt.axis('off')

plt.subplot(3,3,6)
plt.imshow(b, cmap='gray')
plt.axis('off')


plt.subplot(3,3,7)
plt.imshow(m)
plt.axis('off')

plt.show()
