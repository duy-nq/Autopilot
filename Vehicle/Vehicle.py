from ObjectDetector.BaseDetector import BaseDetector
from CollisionHandlingSystem.BaseController import BaseController

class Vehicle:
    def __init__(self, acceleration, detector: BaseDetector, ctr_system: BaseController) -> None:
        self.acceleration = acceleration
        self.detector = detector
        self.controller = ctr_system
        self.signal = 0

        self.actions = {
            'GO': self.proceed,
            'BRAKE': self.brake,
            'TURN_LEFT': lambda: self.rotate('LEFT'),
            'TURN_RIGHT': lambda: self.rotate('RIGHT')
        }
    
    def proceed():
        print('Going ahead')

    def brake():
        print('Break')

    def rotate(direction: str):
        print(f'Turning {direction}')

    def start(self):
        while(1==1):
            self.signal = self.controller.automation()

            if self.signal in self.actions:
                self.actions[self.signal]()
            else:
                print(f'Invalid Signal: {self.signal}')