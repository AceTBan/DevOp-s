def setup():
    size(400, 550)
    stroke(255, 0, 0)
    strokeWeight(50)

x = 50
vx = 3
y = 225
vy = 10

def draw():
    global x,y, vx, vy
    background(0, 0, 255)
    point(x, y)
    x += vx
    if x >= 400 or x < 0:
        vx = -vx
    y += vy
    if y >= 550 or y < 0:
        vy = -vy
