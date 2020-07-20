from math import cos, radians

def cos_correction(value, angle):
    return value * cos(radians(angle))

def adjust_for_angle(data_list):
    temp = []
    for datum in data_list:
        for j in [0, 15, 30, 45, 60, 90]:
            temp.append(cos_correction(datum, j))
    return temp

