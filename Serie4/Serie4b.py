import cv2
import numpy as np


def ex1():
    imgLena = cv2.imread('LenaX.png')
    imgGrey = cv2.imread('LenaX.png', 0)
    mask = 0x0001
    for i in range(0, 8):
        imgRet = cv2.bitwise_and(imgLena, mask)
        imgRet = cv2.normalize(imgRet, None, 0, 255, cv2.NORM_MINMAX)
        mask <<= 1
        cv2.imshow('test', imgRet)
        cv2.waitKey()
        
    mask = 0x00FF
    for i in range(0, 8):
        res = cv2.bitwise_and(imgGrey, mask)
        res = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX)
        mask = (mask << 1) & 0x00FF
        cv2.imshow('grey', res)
        cv2.waitKey()


def ex2():
    imgLena = cv2.imread('LenaX.png')
    imgGrey = cv2.imread('LenaX.png', 0)
    mask = 0x0001
    for i in range(0, 8):
        imgRet = cv2.bitwise_and(imgLena, mask)
        imgRet = cv2.normalize(imgRet, None, 0, 255, cv2.NORM_MINMAX)
        mask <<= 1
        cv2.imshow('test', imgRet)
        cv2.waitKey()

def main():
    ex1()


if __name__ == '__main__':
    main()
