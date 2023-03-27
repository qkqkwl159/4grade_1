import cv2



src = cv2.imread('./img_hw2/peppers.jpg', cv2.IMREAD_COLOR)
rgb_img = cv2.imread('./img_hw2/peppers.jpg',cv2.IMREAD_COLOR)

# RGB 색 평면 분할
b_plane, g_plane, r_plane = cv2.split(src)


# 슬라이싱 이용하여 RGB 색 평면 분할
b_plane = src[:, :, 0]
g_plane = src[:, :, 1]
r_plane = src[:, :, 2]

merg=cv2.merge((b_plane,g_plane,r_plane))
cv2.imshow('rgb', rgb_img)
cv2.imshow('src', src)
cv2.imshow('B_plane', b_plane)
cv2.imshow('G_plane', g_plane)
cv2.imshow('R_plane', r_plane)
cv2.imshow('m',merg)
cv2.waitKey()