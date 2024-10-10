import numpy as np

class BaseController:
    def __init__(self) -> None:
        self.__map = np.ndarray(shape=(4,4), dtype=int)

    def manipulate(self) -> int:
        return 0
    
    def get_map_size(self):
        return self.__map.size
    
    def set_map(self, matrix: np.ndarray):
        self.__map = matrix