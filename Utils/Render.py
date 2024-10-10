import cv2 as cv

COLOR_FOR_CLASS = {
    0: (255, 255, 255),  # White (BGR) for class 0
    1: (0, 0, 255),      # Red (BGR) for class 1
    2: (255, 0, 0),      # Blue (BGR) for class 2
    3: (0, 255, 0),      # Green (BGR) for class 3
    5: (0, 255, 255),    # Yellow (BGR) for class 5
    7: (255, 0, 255),    # Magenta (BGR) for class 7
    9: (128, 0, 128),    # Purple (BGR) for class 9
    10: (255, 165, 0),   # Orange (BGR) for class 10
    11: (0, 128, 128),   # Teal (BGR) for class 11
    12: (255, 192, 203)   # Pink (BGR) for class 12
}

def draw_centered_point(image, vd: list):
    point = [(xywh[0], xywh[1]) for xywh in [xywh[1] for xywh in vd]]
    vclass = [vclass[0] for vclass in vd]

    for i in range(len(point)):
        cv.circle(image, (int(point[i][0]), int(point[i][1])), 5, COLOR_FOR_CLASS.get(vclass[i]), -1)
    
    return image

def display_content(frame, yaxis: int, title: str, content: str):
    text = '{t}: {c}'.format(t=title, c=content)
    return cv.putText(frame, text, (10, yaxis), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)