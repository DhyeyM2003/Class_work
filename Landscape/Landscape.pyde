cloudx = 0
carposition = -500


def setup():
    size (640,480)
    car = loadImage("car.png")
    global car

def draw():
    background(100,100,255)
    
    buildings()
    road(50)
    draw_car(5)
    cloud(0.5)


def buildings():
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

def road(lanex):
    #The road 
    fill(0);
    rect(0,350,640,150)
   
    #The lanes on the road
    fill(255,255,0);
    noStroke();
    ellipse(640,0,100,100)
    
    fill(255,255,0);
    rect(lanex,400, 100,25)
     
    fill(255,255,0);
    rect(lanex + 150,400, 100,25)
     
    fill(255,255,0);
    rect(lanex + 300,400,100,25)

    fill(255,255,0);
    rect(lanex + 450,400, 100,25)

def draw_car(carspeed):
    global carposition
    #moving car
    carposition += carspeed
    image(car,carposition,350,250,70)
    
    #Resetting the car if it goes out of frame
    if carposition == 700:
        carposition = -500

def cloud(cloudspeed):
    global cloudx
    cloudx += cloudspeed
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
