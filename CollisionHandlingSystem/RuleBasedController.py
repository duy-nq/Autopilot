from BaseController import BaseController

class RBC(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def manipulate(self) -> int:
        left_path, right_path = self.evaluate_status(self.__map[0][1]), self.evaluate_status(self.__map[0][2])
        
        if left_path < right_path:
            if left_path == 0 or left_path <= 2 or self.__map[0][0] == 0 or self.__map[0][0] == 2:
                return 2
            else:
                return 1
        elif left_path > right_path:
            if right_path == 0 or right_path <= 2 or self.__map[0][3] == 0 or self.__map[0][3] == 2:
                return 3
            else:
                return 1
        elif left_path == right_path == 0 or left_path == right_path == 2:
            return 0

    def evaluate_status(self, status):
        if status == 0:
            return 0  # Free
        elif status == 1:
            return float('inf')  # Blocked
        elif status == 2:
            return 1  # Small risk
        elif status == 3:
            return 2  # > 50% risk
        elif status == 4:
            return 3  # > 75% risk
        
        return float('inf')
                
             