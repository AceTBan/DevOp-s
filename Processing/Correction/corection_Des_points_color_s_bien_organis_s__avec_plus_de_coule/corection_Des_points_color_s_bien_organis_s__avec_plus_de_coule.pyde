from random import randrange

def setup():
    size(600,600)
    stroke(255,255,255,50)
    noFill()
    background(0)
    strokeWeight(20)
    
def draw():
    for _ in range(100):
        x = randrange(600)
        y = randrange(600)
        stroke(x*255/600,0,y*255/600)
        point(x, y)
