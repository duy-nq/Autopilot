from ObjectDetector.ODv1 import ODv1
from Vehicle.Vehicle import Vehicle
from CollisionHandlingSystem.BaseController import BaseController
from config import get_config

DIRECTION = ['LEFT', 'RIGHT']

def main():
    config = get_config()
    
    test = ODv1('here is the path', 0.5)
    col = BaseController(12)
    v = Vehicle(20, test, col)

    print(v.controller.surrounding_map())

if __name__ == '__main__':
    main()