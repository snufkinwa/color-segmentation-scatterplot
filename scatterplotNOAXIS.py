import cv2
import matplotlib.pyplot as plt
import numpy as np

# When OpenCV first reads the image it is in BGR by default
jellyBean = cv2.imread('jellybean.jpg')
# Convert to RGB
rgbJellyBean = cv2.cvtColor(jellyBean, cv2.COLOR_BGR2RGB)
# Convert to HSV
hsvJellyBean = cv2.cvtColor(jellyBean, cv2.COLOR_RGB2HSV)
# Convert to lab
labImage = cv2.cvtColor(rgbJellyBean, cv2.COLOR_BGR2Lab)


figure, axis = plt.subplots(figsize=(20, 20))
x, y, z = labImage.shape

toPlot = rgbJellyBean.reshape(x*y, 3)
colorsMap = toPlot.astype(np.float_)/256

scatterX = []
scatterY = []
for xi in range(x):
    for yi in range(y):
        L_val = labImage[xi, yi][0]
        A_val = labImage[xi, yi][1]
        B_val = labImage[xi, yi][2]
        scatterX.append(A_val)
        scatterY.append(B_val)

plt.xlabel("FROM GREEN TO RED")
plt.ylabel("FROM YELLOW TO BLUE")
plt.scatter(scatterX, scatterY, c=colorsMap)
plt.show()
