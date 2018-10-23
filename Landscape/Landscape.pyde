cloudx = 0
carposition = -500


def setup():
    size (640,480)
def draw():
    img = loadImage("car.png")
    global cloudx,carposition
    
    background(100,100,255)
    
    #The gray buildings 
    fill(128,128,128);
    rect(0,100,100,250)
    
    fill(128,128,128);
    rect(100,150,100,250)
    
    fill(128,128,128);
    rect(200,130,100,250)
     
    fill(128,128,128);
    rect(300,100,100,250)
    
    fill(128,128,128);
    rect(400,150,100,250)
    
    fill(128,128,128);
    rect(500,90,100,260)
    
    fill(128,128,128);
    rect(600,140,100,260)
   
    
    #The road 
    fill(0);
    rect(0,350,640,150)
   
    #The lanes on the road
    fill(255,255,0);
    noStroke();
    ellipse(640,0,100,100)
    
    fill(255,255,0);
    rect(50,400, 100,25)
     
    fill(255,255,0);
    rect(200,400, 100,25)
     
    fill(255,255,0);
    rect(350,400,100,25)

    fill(255,255,0);
    rect(500,400, 100,25)
    
    #moving car
    carposition += 5
    image(img,carposition,350,250,70)
    
    #Resetting the car if it goes out of frame
    if carposition == 700:
        carposition = -500
    
    
    #Cloud
    cloudx += 0.5
    noStroke();
    fill(255);
    ellipse(cloudx,50,50,50)
    ellipse(cloudx+40,50,50,50)
    ellipse(cloudx+70,50,50,50)
    ellipse(cloudx+25,13,50,50)
    ellipse(cloudx+60,13,50,50)
    
    #Resetting the cloud if it goes out of the screen
    if cloudx == 700:
        cloudx = -100
