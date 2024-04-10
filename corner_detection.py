import numpy as np
import cv2 

img = cv2.imread("assets/chessboard.png")
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey, 100, 0.01, 10)
corners = np.intp(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner_1 = tuple(corners[i][0])
        corner_2 = tuple(corners[j][0])
        colour =tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner_1, corner_2, (colour), 1)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
