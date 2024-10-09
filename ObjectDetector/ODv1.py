from ObjectDetector.BaseDetector import BaseDetector

class ODv1(BaseDetector):
    def __init__(self, model_path, threshold):
        super().__init__(model_path)
        self.threshold = threshold
