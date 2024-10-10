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

## **2. Hardware analysis for choosing model**
Many factors could 'affect' in the model selection stage
- Better model, lower performance!
- Cam: 24fps, but should care about 12 or 6 for better performance (need to think about their speed) 
- Table for consideration
- Conclusion

About road detection
- Better if it was a combination between MAPS and real-time footage, know about the planned trip will help, too.
- So far, hard to perform in such 03 days -> use alternative (easy) approach: "area of interested"!.

## **3. Object detection**
Based on my analysis and observations, these are the classes we should be interested in. The limitation on the classes the model can recognize is likely to the situation that the model only be trained with a small number of 'street' objects.
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
| .. | many more       | n/a   |

I also set the maximum **number of detection objects** and minimum **confident** for better performance.

After finishing this stage, data will be transfrom into an *estimated matrix*.

## **4. Novel object detection**
I do know this is the hardest part for any AI model nowadays. For only 03 days, I only find out this "solution":

First, find all recognizable objects and "remove" them from the frame by painting them white.

Next, focus on *region of interest* (roi) and using simple aprroach:
- Detect edges from the frame and calculate total of white pixel.
- Split the 'image' edges into 4 parts. Calculate the 'pixel intensity' for each part and compare it to some threshold (0.5, 0.25, etc). With that, I'm trying to figure out the distribution of white pixels... It comes from the usual idea: 'each part should contain 25% on average'.
- Based on these value, I label it on the *estimated matrix* with the possible value in range of 2 to 4 (higher value, higher probability that it will be a novel object).

But this approach is too naive, to be honest! Wrong detection is likely to happen because I haven't figure out how to focus on the crucial aspect: **ROAD/STREET**

# **CONS**
Use fixed 'size of matrix' for RuleBasedController

# **VERY LAST WORD**