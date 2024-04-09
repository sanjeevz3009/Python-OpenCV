import cv2
import random

img = cv2.imread("assets/python.png", 1)
# img = cv2.resize(img, (0, 0), fx=5, fy=5)
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imwrite("assets/updated_python.png", img)

# cv2.imshow("Pic", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(img[250:400])

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
