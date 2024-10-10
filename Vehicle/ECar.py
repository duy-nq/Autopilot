from CollisionHandlingSystem.BaseController import BaseController
from ObjectDetector.BaseDetector import BaseDetector
from Vehicle.Vehicle import Vehicle
from Utils.Render import display_content
import cv2 as cv

class ECar(Vehicle):
    def __init__(self, acceleration: int, detector: BaseDetector, ctr_system: BaseController) -> None:
        super().__init__(acceleration, detector, ctr_system)
        self.actions['REVERSE'] = self.reverse
        self.FRAME_TO_SKIP = 15

    def reverse() -> str:
        return 'Reserving'
    
    def proceed() -> str:
        return 'Going ahead'
    
    def idle() -> str:
        return 'Using break'
    
    def rotate(direction: str) -> str:
        return f'Turning {direction}'

    def start(self):
        live_capture = self.extract_video()
        frame_to_cap = 0
        
        while(live_capture.isOpened()):
            ret, frame = live_capture.read()
            live_capture.set(cv.CAP_PROP_POS_FRAMES, frame_to_cap)
            
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            displayed_frame, detected_frame, estimated_matrix_v1 = self.detector.object_detection(frame)
            estimated_matrix_v2 = self.detector.novel_detection(detected_frame, estimated_matrix_v1)
            
            self.controller.set_map(estimated_matrix_v2)
            self.signal = self.controller.manipulate()

            if self.signal in self.actions:
                action = self.actions[self.signal]()
                display_content(displayed_frame, 50, 'ACTION', action)
            else:
                print(f'Invalid Signal: {self.signal}')

            cv.imshow(displayed_frame)
            frame_to_cap += self.FRAME_TO_SKIP
            if cv.waitKey(1) == ord('q'):
                break

    