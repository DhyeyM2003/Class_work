"""
This program starts off by drawing three stars (make sure it works).
Do the following in steps:
1. Increase the number of stars to 5.
2. Rather than calling an ellipse function for each star, 
   create a while loop with an index variable to draw them.
3. Rather than manually adding stars, create a for loop that will add 100
   stars to the stars_x and stars_y lists with random x/y coordinates.
4. Create a for loop to increase the x location ever so slightly to make the 
   stars move across the sky.
5. Within the draw loop, use the list.append() method on both lists to 
   periodically add another star. Add the star off-screen and let it move into view.
   - You need to limit the number of times per second a new star is added, or there
     will be too many created (60 per second). Use frameCount % 60 == 0 to create one every 60 frames.
6. If any particular star has moved out of view, remove it from the lists. Use list.pop(index) to remove
   the appropriate coordinates.
"""

# two lists with three stars' xy coordinates
# (50, 200), (100, 250), (150, 300)

import random

def setup():
    global star
    size(640, 480)
    star = [[],[]]
    for i in range(100):
        star[0].append(random.randint(0,640))
        star[1].append(random.randint(0,480))


def draw():
    background(0)
    
    # draw stars
    noStroke()
    fill(255)
    
    for i in range(len(star[0])):
        star[0][i] += 1
        ellipse(star[0][i],star[1][i],5,5)
    
    if frameCount % 6 == 0:
        star[0].append(-1)
        star[1].append(random.randint(0,480))
    
    for index in range(len(star[0])):
            try:
                if star[0][index] > 640:
                    star[0].pop(index)
                    star[1].pop(index)
            except:
                break
