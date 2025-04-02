
import cv2
import numpy as np

def main():
    img = cv2.imread("img.png", 0)

    equ = cv2.equalizeHist(img)

    # stacking images side-by-side
    res = np.hstack((img, equ))

    # show image input vs output
    cv2.imshow('image', res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
