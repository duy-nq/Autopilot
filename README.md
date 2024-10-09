# **PROTOTYPE**
## **1. Overview**
Road detection will be played a crucial role while doing task A and B

Novel object detection will be based on threshold?

Flow:
- Video footage
- Road (lane) detection (perform better when we have a map)
- Vehicle, people detection + novel obj. recognize -> surrounding_map
- Rule based system to control a car via surrounding_map

How to detect a road?
- Focus on main part

System analyst:
- Small VRAM, balancing both accuracy on detection and real-time process

Rule for controlling stage:
- BLOCK rotate to the left or right if there is obstacle in a limit range
- SLOW DOWN when reach the minimum distance with the up-front vehicles
- GO AHEAD if everything is all free

Limited object for detection
- Car, Truck,...
- Number of obj for each detection

## **2. Analyze**
Many factors could 'affect' in the model selection stage
- Better model, lower performance!
- Cam: 24fps, but should care about 12 or 6 for better performance (need to think about their speed) 
- Table for consideration
- Conclusion

About road detection
- Better if it was a combination between MAPS and real-time footage, know about the planned trip will help, too.
- So far, hard to perform in such 03 days -> use alternative (easy) approach: "area of interested"!