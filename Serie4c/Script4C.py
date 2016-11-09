import cv2
import numpy as np
from matplotlib import pyplot as plt


def ex3():
    img = cv2.imread('LenaX.png')

    ker = np.ones((3, 3), np.float32) / 9
    ker2 = np.matrix([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    ker3 = np.matrix([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    ker4 = np.matrix([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    ker5 = np.matrix([[-1, -1, -1], [-1, 12, -1], [-1, -1, -1]])/4


    dst = cv2.filter2D(img, -1, ker5)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

    cv2.waitKey(0)


def main():
    print('serie 4c')
    ex3()


if __name__ == "__main__":
    main()
