from random import randrange
    
def setup():
    
    size(720, 680)
    stroke(255, 255, 0)
    strokeWeight(5)

    global all_x, all_y, all_vx, all_vy,x,y, vx, vy
   
    brique = randrange (1,11)
    
    x = 50
    vx = 3
    y = 225
    vy = 10

    all_x = []
    all_vx = []
    all_y = []
    all_vy = []
        
    for _ in range(brique):

        all_x.append(randrange(5,width-5))
        all_y.append(randrange(5,height-5))

def draw():
    global x,y, vx, vy

    background(0)
    line(mouseX,650,mouseX+100,650)
    ellipse(x, y, 12, 12)
    x += vx
    if x >= width or x < 0:
        vx = -vx
    y += vy
    if y >= height or y < 0:
        vy = -vy
    
    
    for i in range(len(all_x)):
        rect(all_x[i], all_y[i],0,0)

        if all_x[i] >= width or all_x[i] < 0:
            all_vx[i] = -all_vx[i]

        if all_y[i] >= height or all_y[i] < 0:
            all_vy[i] = -all_vy[i]    
            
# fait disparaitre les briques
#     if len(all_x) > 0:
#         all_x.pop()
#         all_y.pop()
