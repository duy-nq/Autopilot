import numpy as np

class BaseController:
    def __init__(self, safe_distance) -> None:
        self.__nov = 0
        self.__safe_distance = safe_distance
        self.__map = np.ndarray(shape=(4,4), dtype=int)

    def automation(self) -> int:
        return 0