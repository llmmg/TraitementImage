import cv2
import numpy as np
from matplotlib import pyplot as plt


def normalize():
    img = cv2.imread('Unequalized_Hawkes_Bay_NZ.bmp', 0)

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()

    cv2.imshow("derpderp", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[img]

    cv2.imshow("derp", img2)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()

    plt.plot(cdf_normalized, color='b')
    plt.hist(img2.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


def clahe():
    # cumulated histogram

    img = cv2.imread('marseilleBW.tif', 0)
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(10, 10))
    cl1 = clahe.apply(img)

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()

    ##image
    cv2.imshow('clahe', cl1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ## histogram after transformation
    hist, bins = np.histogram(cl1.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    plt.plot(cdf_normalized, color='b')
    plt.hist(cl1.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


def main():
    # hehehe
    # img = cv2.imread('Unequalized_Hawkes_Bay_NZ.bmp', 0)
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()

    # normalize()
    clahe()


if __name__ == '__main__':
    main()
