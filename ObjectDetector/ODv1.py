from ObjectDetector.BaseDetector import BaseDetector
from ultralytics import YOLO
import cv2 as cv
from Utils.Transform import *
from Utils.Render import draw_centered_point
import numpy as np

class ODv1(BaseDetector):    
    """
    Detect based on YOLO pretrain model!
    """
    
    def __init__(self, model_path, max_obj: int, min_conf: float, threshold:int):
        super().__init__(model_path)
        self.model = YOLO(self.model_path)
        self.classes = [0,1,2,3,5,7,9,10,11,12]
        self.max_obj = max_obj
        self.min_conf = min_conf
        self.threshold = threshold

    def calculate_estimated_matrix(self, boxes: list, frame_size: tuple, matrix = np.ndarray((4,4), dtype=int)) -> np.ndarray:
        """
        Image to (4,4) ndarray with x-axis is "left to right" and y-axis is "near to far"
        """

        for box in boxes:
            x_center, y_center, _, height = box
            row, col = 0, 0
            alt_point = (y_center + height) / frame_size[0]

            if x_center < frame_size[1] / 4:
                col = 0
            elif x_center < frame_size[1] / 2:
                col = 1
            elif x_center < 3 * frame_size[1] / 4:
                col = 2
            else:
                col = 3

            if alt_point > 0.9:
                row = 0
            elif alt_point > 0.7:
                row = 1
            elif alt_point > 0.5:
                row = 2
            else:
                row = 3

            matrix[row, col] = 1

        return matrix

    def object_detection(frame, self):
        def remove(boxes):
            frame_cp = frame.orig_img.copy()
            
            for box in boxes:
                x_center, y_center, width, height = box

                x1 = x_center - width // 2
                y1 = y_center - height // 2

                frame_cp[y1:y1+height, x1:x1+width] = (255, 255, 255)

            return frame_cp
        
        result = self.model.predict(frame, 
                                    device='0', 
                                    classes=self.classes, 
                                    max_det=self.max_obj, 
                                    conf=self.max_conf)
        
        box_and_class = zip(tensor_list_to_int(result.boxes.cls),
                            tensor_to_float(result.boxes.xywh))
        
        estimated_matrix = self.calculate_estimated_matrix(box_and_class[1], frame.shape[:2])
        modified_image = remove(box_and_class[1])
        draw_centered_point(frame, box_and_class)  

        return modified_image, estimated_matrix

    def novel_detection(frame, matrix: np.ndarray):
        height, width, _ = frame.shape
        roi = frame[int(height * 3 / 4):height, int(width/4):int(width*3/4)]

        edges = cv.Canny(cv.cvtColor(roi, cv.COLOR_BGR2GRAY), 50, 50)
        white_pixel = np.sum(edges == 255)

        cropped_edges = [
            edges[:,:int(edges.shape[1]/4)],
            edges[:,int(edges.shape[1]/4):int(edges.shape[1]*2/4)],
            edges[:,int(edges.shape[1]*2/4):int(edges.shape[1]*3/4)],
            edges[:,int(edges.shape[1]*3/4):]
        ]

        pixel_intensity = [np.sum(ce == 255)/white_pixel for ce in cropped_edges]

        for i in range(len(pixel_intensity)):
            if pixel_intensity[i] > 0.5:
                matrix[0][i] == 4
            elif pixel_intensity[i] > 0.25:
                matrix[0][i] == 3
            elif pixel_intensity[i] > 0.15:
                matrix[0][i] == 2

        return matrix
