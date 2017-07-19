import cv2
import numpy as np

cv2.namedWindow('app')
cv2.createdTrackbar('contrast', 'app', 1)

while True:
	k = cv2.waitKey(1) & 0xFF
	if k == ord('q'):
		break

cv2.destroyAllWindows()