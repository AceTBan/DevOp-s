
def setup():
    size(720,250)
    background(0)
    stroke(255)
    frameRate(60)

    global c
    c = 0
    global mode
    mode=0
  
def draw():
    print (mouseX,mouseY)
    
    global c
    c= (c+1)%256
    
    for i in range(width):
        r = random(255)
        point(i,r)
        
    if mode == 0:
        stroke(c,0,0)
    elif mode == 1:
        stroke(0,c,0)
    else:
        stroke(0,0,c)
        
    c = color(random(255),random(255),random(255))    
    


    global mode
    mode = (mode+1)%3

    
    
    
    
    
