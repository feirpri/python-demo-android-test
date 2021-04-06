from utils.getStringPosition import *
import numpy as np
import cv2
from pytesseract import image_to_string

# 按行找到有文字的区域进行分割
def line_row_boundary(gray_img):
    text_boundary_by_row = []
    last_boundary = 0
    for index in range(len(gray_img)):
        no_text = min(gray_img[index]) == max(gray_img[index])
        if index + 1 == len(gray_img):
            is_boundary = True
        else:
            next_no_text = min(gray_img[index+1]) == max(gray_img[index+1])
            is_boundary = no_text != next_no_text

        if is_boundary:
            if not no_text:
                text_boundary_by_row.append((last_boundary, index, gray_img[last_boundary:index + 1, 0:].copy))
                cv2.line(img, (0, last_boundary), (width, last_boundary), (0, 200, 127))
                cv2.line(img, (0, index), (width, index), (0, 200, 127))
            last_boundary = index

def test():
    oo = cv2.imread('../settings.png', -1)
    print(len(get_string_position(oo)))

    oo = cv2.imread('../settings.png', -1)
    oo = cv2.threshold(oo, 150, 255, cv2.THRESH_BINARY)[1]
    print(len(get_string_position(oo)))
