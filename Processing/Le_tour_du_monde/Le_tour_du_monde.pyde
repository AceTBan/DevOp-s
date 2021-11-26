def setup():
    size(400, 600)
    stroke(255, 0, 0)
    strokeWeight(50)

x=0
y=0

def draw():
    global x,y
    background(0, 0, 255)
    point(x%width,y%height)
    x+=1
    y+=2
