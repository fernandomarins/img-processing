import cv2
import numpy as np

def dummy(val):
	pass


img = 'paisagem.jpg'
identity_kernel = np.array([
	[0, 0, 0],
	[0, 1, 0],
	[0, 0, 0]
])

sharpen_kernel = np.array([
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]
])

box_kernel = np.array([
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]
], np.float32) / 9 #we added np.float to make sure the result is a float and /9 because the kernel is declared this way

gaussian_kernel_1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel_2 = cv2.getGaussianKernel(5, 0)
kernels = [identity_kernel, sharpen_kernel, box_kernel, gaussian_kernel_1, gaussian_kernel_2]

color_original = cv2.imread(img)
#it's necessary to have two images because you change the settings of one but you always
#want to keep the original one
color_modified = color_original.copy()

cv2.namedWindow('app')
cv2.createTrackbar('contrast', 'app', 1, 100, dummy) #(name, window name, initial value, maximum value, callback)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels) - 1, dummy) #we added len(kernels) - 1 so we can just add new kernels without changing this value every time
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

while True:
	cv2.imshow('python.png', color_modified)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('q'):
		break

	#to keep track of trackbar position
	contrast = cv2.getTrackbarPos('constrast', 'app')
	brightness = cv2.getTrackbarPos('brightness', 'app')
	kernel = cv2.getTrackbarPos('filter', 'app')

	color_modified = cv2.filter2D(color_original, -1, kernels[kernel])

	#the brightness and constrant are calculated 
	color_modified = cv2.addWeighted(color_original,
									constrast, np.zeros(color_original.shape, dtype=color_original.dtype), 0, 
									brightness - 50) #we added 50 because it's the initial value for brigthness

cv2.destroyAllWindows()