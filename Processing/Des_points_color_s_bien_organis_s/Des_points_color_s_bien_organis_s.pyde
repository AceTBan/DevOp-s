x=random(255)

def setup():
    size(720,250)
    background(0)
    stroke(255)
    frameRate(60)

def draw():
    print (mouseX,mouseY)

    
    for i in range(width):
        r = random(255)
        point(i,r)

        stroke (x,0,255)
        
