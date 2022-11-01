test_h = int(input("Heigth of wall:"))
test_w = int(input("Width of wall:"))

coverage = 5

import math

def paint_calc(height=test_h, width=test_w, c=coverage):
    number_of_cans = ((height*width)/coverage)
    return round(number_of_cans)

print(paint_calc())