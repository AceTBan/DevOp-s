from random import randrange
    
def setup():
    
    size(1000, 400)
    stroke(255, 0, 0)
    strokeWeight(50)

    global all_x, all_y, all_vx, all_vy
   
    ball = randrange (1,10)

        
    all_x = []
    all_vx = []
    all_y = []
    all_vy = []
        
    for _ in range(ball):

        all_x.append(randrange(5,width-5))
        all_y.append(randrange(5,height-5))
        all_vx.append(randrange(-5,5))
        all_vy.append(randrange(-5,5))

def draw():
    
    background(0, 0, 255)

    
    
    for i in range(len(all_x)):
        point(all_x[i], all_y[i])
        all_x[i] += all_vx[i]
        if all_x[i] >= width or all_x[i] < 0:
            all_vx[i] = -all_vx[i]
        all_y[i] += all_vy[i]
        if all_y[i] >= height or all_y[i] < 0:
            all_vy[i] = -all_vy[i]    
            
            
            
            
            
            
            
            
        
            
