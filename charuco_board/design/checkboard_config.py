import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cv2
from cv2 import aruco


squaresX = 7                           # Number of squares in X direction
squaresY = 6                           # Number of squares in Y direction
squareLength = 300                      # Square side length (in pixels)
markerLength = 225                      # Marker side length (in pixels)
margins = (squareLength - markerLength) * 2
borderBits = 1                      

imageSize = np.array([squaresX, squaresY]) * squareLength + 2 * margins

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)

board = aruco.CharucoBoard_create(squaresX, squaresY, squareLength, markerLength, aruco_dict)

imboard = board.draw(imageSize, marginSize = margins, borderBits = borderBits)
cv2.imwrite("charucoboard_design_check.png", imboard)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.imshow(imboard, cmap = mpl.cm.gray)#, interpolation = "nearest")
ax.axis("off")
plt.show()
