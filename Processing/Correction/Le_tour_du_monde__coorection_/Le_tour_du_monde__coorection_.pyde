#Balle en version temporelle
def setup():
    size(200, 550)
    stroke(255, 0, 0)
    strokeWeight(50)

t = 0

def draw():
    global t
    background(0, 0, 255)
    point(t%200, t%550)
    t+=1
