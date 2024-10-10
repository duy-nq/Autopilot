from ObjectDetector.BaseDetector import BaseDetector
from CollisionHandlingSystem.BaseController import BaseController
import cv2 as cv

class Vehicle:
    def __init__(self, acceleration: int, detector: BaseDetector, ctr_system: BaseController, path: str) -> None:
        self.acceleration = acceleration
        self.detector = detector
        self.controller = ctr_system
        self.signal = 0
        self.video_path = path

        self.actions = {
            'GO': self.proceed,
            'IDLE': self.idle,
            'TURN_LEFT': lambda: self.rotate('LEFT'),
            'TURN_RIGHT': lambda: self.rotate('RIGHT')
        }
    
    def proceed():
        print('Going ahead')

    def idle():
        print('Using break')

    def rotate(direction: str):
        print(f'Turning {direction}')

    def extract_video(self):
        return cv.VideoCapture(self.video_path)

    def start(self):
        pass