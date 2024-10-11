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

About road detection
- Better if it was a combination between MAPS and real-time footage, know about the planned trip will help, too.
- So far, hard to perform in such 03 days -> use alternative (easy) approach: "area of interested"!.

## **2. Hardware analysis for choosing model**
For this project, I have 16GB of RAM and 2GB of VRAM (I am using GPU MX-250). This settings is not very good for real-time decision problem, to be honest!

We all know that it takes time for the model to recognize things and perform some calculations. Assume that the camera provide us 30 frames per second (fps), so we should do all of these tasks in less than 1/30 second.

It will be easy with the good hardware, we can implement a better model to improve accuracy while maintaining the performance nicely. In contrast, as I mentioned before, I don't have that fancy GPU so I had to carefully considerate between accuracy and performance.

Here is what I got after experiment:

| Size of model                | Nano   | Small   | Medium  | Large   | Extra large |
| ---------------------------- | ------ | ------- | ------- | ------- | ----------- |
| Time to resolve a frame (ms) | 68~70  | 158~176 | 385~410 | 690~735 | 1100~1150   |

Sometimes, we don't need to care about all of the frames that we got from the camera. In my last project, when I have faced the task 'counting vehicle' and I chose 3/30 frames to solved (1st, 15th and 30th) and it worked. The main reason is the footage was taken on a busy street in the city, where maximum speed I saw was 20-35km/h, and these 03 frames rarely miss counting these vehicle.

Speaking of controlling vehicle automatically, we should be more careful. Based on the limited speed on the road, they could drive at 80km/h or more than that! Then, choosing only 03 frames cannot help us monitor the situation. With all of my analysis above, I chose a **nano** model with 03 frames to skip (solve 10 frames per second) to balance between two important factors: **accuracy** and **performance**.

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
- Split the 'image' edges into 4 parts. Calculate the 'pixel intensity' for each part and compare it to some threshold (0.5, 0.25, etc). With that, I'm trying to figure out the distribution of white pixels... It comes from the idea: 'each part should contain 25% on average'.
- Based on these value, I label it on the existing *estimated matrix* with the possible value in range of 2 to 4 (higher value, higher probability that it will be a novel object).

But this approach is too naive, to be honest! Wrong detection is likely to happen because I haven't figure out how to focus on the crucial aspect: **ROAD/STREET**

One more thing, I haven't visualize the data of possible 'area' that could contain novel object on the frame. It was a big omission!

## **5. Rule Based Control (RBC) System**
As the same as the title, I use RBC to control the car, the decisions are made using data collected from Object Detection Model.

My idea is trying to convert data after the detection stage into a 4x4 matrix (for now). With x-axis represents **'left to right'** while y-axis represents **'near to far'**.

Possible values for those elements in the matrix:
- 0: Free
- 1: Detected Object
- 2: 25% chances of novel object
- 3: 50% chances of novel object
- 4: 75% chances of novel object

The vehicles don't have to idle when they are facing 0 and 2. In the others case, things will have to be considerate!

Assume that we are in center of the matrix (the line seperate matrix into a half). There are some situtation that could happen:
- Free road ahead us: Go ahead or rotate in 'any' directions as you want.
- Left side is free, Right side isn't; and vice versa: Based on the matrix to decide.
- Both sides are blocked: Idle our car and wait!

What is the role of others values in the matrix? For the most left and right, I think I could use it to prevent the car turning into something that they couldn't. I haven't thought about this problem clearly, so I haven't implemented it yet (because it contains many 'edge' cases).

Why I choose a 4x4 matrix? It based on my thought of 'rural' area, and with the data that I have - the car drive on a small road. Better size of the matrix, the higher chances of control the vehicle correctly; besides, continuing to use RBC in this case will be a challenge.

The fixed sized of matrix for now is the problem because we can't assure that any 'rural' areas has the small roads. This is not flexible but it was easy for me to apply some simple rules (the space of possible things that could happen is smaller).

# **FINAL THOUGHTS**
I would like to extend my sincere gratitude to Delta Cognition for the opportunity to participate in this test. It has presented numerous challenges and aspects that I have not encountered before, greatly enriching my experience.