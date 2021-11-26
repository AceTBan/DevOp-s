def setup():
    size(600,600)
    stroke(255)
    noFill()
    
def draw():
    background(0)
    forme_bizarre(300,300)
    forme_bizarre(150,150)
    forme_bizarre(450,150)
    forme_bizarre(150,450)
    forme_bizarre(450,450)
    forme_bizarre(mouseX,mouseY)
    
    
    
# Je crée mon outil forme_bizarre
# x : abscisse où faire le dessin
# y : ordonnée où faire le dessin
def forme_bizarre(x,y):
    circle(x,y,100)
    ellipse(x,y,100,50)
    ellipse(x,y,50,100)
    circle(x,y,50)
