import cv2

img = cv2.imread("assets/python.png", 0)
img = cv2.resize(img, (0, 0), fx=5, fy=5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("assets/updated_python.png", img)

cv2.imshow("Profile Pic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
