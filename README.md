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
- So far, hard to perform in such 03 days -> use alternative (easy) approach: "area of interested"!.

| ID | Object          | Used? |
|----|-----------------|-------|
| 0  | person          | Yes   |
| 1  | bicycle         | Yes   |
| 2  | car             | Yes   |
| 3  | motorcycle      | Yes   |
| 4  | airplane        | No    |
| 5  | bus             | Yes   |
| 6  | train           | No    |
| 7  | truck           | Yes   |
| 8  | boat            | No    |
| 9  | traffic light   | Yes   |
| 10 | fire hydrant    | Yes   |
| 11 | stop sign       | Yes   |
| 12 | parking meter   | Yes   |

## **3. Novel detection**
I do know this is the hardest part for any AI model nowadays. For only 03 days, I only find out this "solution":

First, find all recognizable objects and "remove" them from the frame by painting them white.

Next, focus on area of interest and using simple aprroach:
- Detect edges on the image, invert to find areas without edges (1). Then exclude the area belonging to the detected object (if any).
- Slice a window on the image to find out 'pixels intensity' matrix

# **CONS**
Use fixed 'size of matrix' for RuleBasedController

# **VERY LAST WORD**
