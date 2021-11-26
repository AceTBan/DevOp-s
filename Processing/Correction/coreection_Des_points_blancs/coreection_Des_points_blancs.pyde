from random import randrange

def setup():
    size(600,600)
    stroke(255,255,255,50)
    noFill()
    background(0)
    strokeWeight(20)
    
def draw():
    for _ in range(100):
        point(randrange(600), randrange(600))
        
        
        
        
        
# from random import randrange

# def setup():
#     size(600,600)
#     stroke(255,255,255,50)
#     noFill()
#     background(0)
#     strokeWeight(20)
    
# def draw():
#     for _ in range(100):
#         stroke(randrange(255),0,randrange(200,255),50)
#         point(randrange(600), randrange(600))
