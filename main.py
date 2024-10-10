from ObjectDetector.ODv1 import ODv1
from Vehicle.Vehicle import Vehicle
from CollisionHandlingSystem.RuleBasedController import RBC
from config import get_config

def main():
    config = get_config()
    
    detector = ODv1(config.model_path, config.threshold)
    controller = RBC(12)
    v = Vehicle(20, detector, controller)

    v.start()

if __name__ == '__main__':
    main()