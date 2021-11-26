def setup():
    size(1000, 400)
    stroke(255, 0, 0)
    strokeWeight(50)

# x = 50
# vx = 3
# y = 225
# vy = 10

# x2 = 150
# vx2 = 3
# y2 = 325
# vy2 = 10

all_x = [50,150,50,70,80,90]
all_vx = [3,3,7,-5,6,0]
all_y = [225,325,100,200,100,398]
all_vy = [10,10,0,-7,2,3]

def draw():
    background(0, 0, 255)
    
    # global x,y, vx, vy
    # point(x, y)
    # x += vx
    # if x >= 400 or x < 0:
    #     vx = -vx
    # y += vy
    # if y >= 550 or y < 0:
    #     vy = -vy
        
    # global x2,y2, vx2, vy2
    # point(x2, y2)
    # x2 += vx2
    # if x2 >= 400 or x2 < 0:
    #     vx2 = -vx2
    # y2 += vy2
    # if y2 >= 550 or y2 < 0:
    #     vy2 = -vy2
    
    global all_x, all_y, all_vx, all_vy
    for i in range(len(all_x)):
        point(all_x[i], all_y[i])
        all_x[i] += all_vx[i]
        if all_x[i] >= width or all_x[i] < 0:
            all_vx[i] = -all_vx[i]
        all_y[i] += all_vy[i]
        if all_y[i] >= height or all_y[i] < 0:
            all_vy[i] = -all_vy[i]
