def setup():
    size(200, 600)
    stroke(255, 0, 0)
    strokeWeight(50)

x = 0

def draw():
    global x
    background(0, 0, 255)
    point(x, 300)
    x = (x+1)%200
    print(x)
