from BaseController import BaseController

class RBC(BaseController):
    def __init__(self, safe_distance) -> None:
        super().__init__(safe_distance)

    def process(self):
        return 'GO'