from scipy import ndimage, misc
import imageio
import numpy as np
import os
import cv2 as cv


def main():

    gamma = 0.5

    lookUpTable = np.empty((1, 256), np.uint8)

    outPath = "/Users/drewmichelini/Images/output"
    path = "/Users/drewmichelini/Images/input/"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        img_original = imageio.imread(input_path)

        for i in range(256):
            lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
        res = cv.LUT(img_original, lookUpTable)

        # create full output path, 'example.jpg'
        # becomes 'adjusted_example.jpg', save the file to disk
        fullpath = os.path.join(outPath, 'adjusted_' + image_path)
        imageio.imwrite(fullpath, res)
        #(255.0 * img_original).astype('uint8')

if __name__ == '__main__':
    main()
