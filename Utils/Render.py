import cv2 as cv

COLOR_FOR_CLASS = {
    1: (0, 0, 255),    # Red (BGR)
    3: (0, 255, 0),    # Green (BGR)
    2: (255, 0, 0),    # Blue (BGR)
    5: (0, 255, 255),  # Yellow (BGR)
    7: (255, 0, 255)   # Magenta (BGR)
}

def draw_centered_point(image, vd: list):
    point = [(xywh[0], xywh[1]) for xywh in [xywh[2] for xywh in vd]]
    vclass = [vclass[0] for vclass in vd]

    for i in range(len(point)):
        cv.circle(image, (int(point[i][0]), int(point[i][1])), 5, COLOR_FOR_CLASS.get(vclass[i]), -1)
    
    return image

def display_content(frame, yaxis: int, title: str, content: str):
    text = '{t}: {c}'.format(t=title, c=content)
    return cv.putText(frame, text, (10, yaxis), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)