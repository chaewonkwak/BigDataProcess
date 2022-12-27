!/usr/bin/python3

import numpy as np
import cv2
import glob
import re

FILE_NAME = 'trainingDigits'

def load_train_data(file_name):
        with np.load(file_name) as data:
                train = data['train']
                train_labels = data['train_labels']
        return train, train_labels

def resize20(image):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GBRAY)
        gray_resize = cv2.resize(gray, (20, 20))
        plt.imshow(cv2.cvtColor(gray_resize, cv2.COLOR_GRAY2RGB))
        plt.show()
        return gray_resize.reshape(-1, 400).astype(np.float32)

def check(test, train, train_labels, k):
        knn = cv2.ml.KNearest_create()
        knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
        ret, result, neighbours, dist = knn.findNearest(test, k)

def errorCheck(k):

        train, train_labels = load_train_data(FILE_NAME)
        errorCount = 0.0
        numTestVecs = int(train.shape[0]*0.10)

        for file_name in glob.glob('./testDigits'):
                test = resize20(file_name)
                answer = 0
                result = check(test, train, train_labels, k)
                for i in file_name:
                        answer = re.findall(r"(\d+)", i)[0]
                if (int(result) != int(answer)):
                        errorCount += 1.0
        print "%d\n" % (errorCount / numTestVecs)


for i in range(20):
        errorCheck(i + 1)
