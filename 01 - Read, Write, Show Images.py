import cv2

# 0 - gray, 1 color, -1 color with alpha
img = cv2.imread('lena.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

# Press esc for destroy
if k == 27:
  cv2.destroyAllWindows()

# Press s to save image
elif k == ord('s'):
  cv2.imwrite('lena_copy.png', img)
  cv2.destroyAllWindows()