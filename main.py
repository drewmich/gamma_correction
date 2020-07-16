#!/usr/bin/env python
import imageio
import numpy as np
import os
import cv2 as cv
import sys


def main():



    lookUpTable = np.empty((1, 256), np.uint8)

    outPath = sys.argv[1]
    #"/Users/drewmichelini/Images/output"
    path = sys.argv[2]
    #"/Users/drewmichelini/Images/input/"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # make the input path and read the file
        input_path = os.path.join(path, image_path)
        img = imageio.imread(input_path)

        if (sys.argv[3] == "clahe"):
            # convert to grayscale
            gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # create a CLAHE object (Arguments are optional).
            clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            cl1 = clahe.apply(gray_image)

            fullpath = os.path.join(outPath, 'adjusted_' + image_path)
            imageio.imwrite(fullpath, cl1)

        if (sys.argv[3] != "clahe"):

            gamma = .95
            for i in range(256):
                lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
            res = cv.LUT(img, lookUpTable)

            # makes path for output
            fullpath = os.path.join(outPath, 'adjusted_' + image_path)
            imageio.imwrite(fullpath, res)


if __name__ == '__main__':
    main()
