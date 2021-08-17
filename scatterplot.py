import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

# When OpenCV first reads the image it is in BGR
jellyBean = cv2.imread('jellybean.jpg')
# Convert to RGB
rgbJellyBean = cv2.cvtColor(jellyBean, cv2.COLOR_BGR2RGB)
# Convert to HSV
hsvJellyBean = cv2.cvtColor(jellyBean, cv2.COLOR_RGB2HSV)


r, g, b = cv2.split(rgbJellyBean)
figure = plt.figure()
axis = figure.add_subplot(1, 1, 1, projection="3d")

pixelColors = rgbJellyBean.reshape((np.shape(rgbJellyBean)[0]*np.shape(rgbJellyBean)[1], 3))
norm = colors.Normalize(vmin=-1., vmax=1.)
norm.autoscale(pixelColors)
pixelColors = norm(pixelColors).tolist()

axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors = pixelColors, marker=".")
axis.set_xlabel("RED")
axis.set_ylabel("GREEN")
axis.set_zlabel("BLUE")
plt.show()
