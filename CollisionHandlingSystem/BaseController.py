import numpy as np

class BaseController:
    def __init__(self, safe_distance) -> None:
        self.__map = np.ndarray(shape=(4,4), dtype=int)

    def automation(self) -> int:
        return 0
    
    def get_map_size(self):
        return self.__map.size