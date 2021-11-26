from random import randrange
    
def setup():
    size(1000, 400)
    stroke(255, 0, 0)
    strokeWeight(50)
    for _ in range(6):
        add_random_ball()

all_x = []
all_vx = []
all_y = []
all_vy = []
sizes = []
r = []
g = []
b = []

def add_random_ball():
    global all_x, all_y, all_vx, all_vy
    all_x.append(randrange(width))
    all_y.append(randrange(height))
    all_vx.append(randrange(-10,10))
    all_vy.append(randrange(-10,10))
    sizes.append(randrange(1,50))
    r.append(randrange(255))
    g.append(randrange(255))
    b.append(randrange(255))
    
def draw():
    background(0, 0, 255)
    global all_x, all_y, all_vx, all_vy

    for i in range(len(all_x)):
        strokeWeight(sizes[i])
        stroke(r[i], g[i], b[i])
        point(all_x[i], all_y[i])
        all_x[i] += all_vx[i]
        if all_x[i] >= width or all_x[i] < 0:
            all_vx[i] = -all_vx[i]
        all_y[i] += all_vy[i]
        if all_y[i] >= height or all_y[i] < 0:
            all_vy[i] = -all_vy[i]
            
def mouseClicked():
    add_random_ball()
    
def keyPressed():
    if len(all_x) > 0:
        all_x.pop()
        all_y.pop()
        all_vx.pop()
        all_vy.pop()
        sizes.pop()
        r.pop()
        g.pop()
        b.pop()
