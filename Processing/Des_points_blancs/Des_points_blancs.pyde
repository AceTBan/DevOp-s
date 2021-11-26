
def setup():
    size(800,250)
    background(0)
    stroke(255)
    frameRate(100)
    
def draw():
    print(mouseX,mouseY)
    
    for i in range(width):
        r = random(255)
        point(i,r)

  
