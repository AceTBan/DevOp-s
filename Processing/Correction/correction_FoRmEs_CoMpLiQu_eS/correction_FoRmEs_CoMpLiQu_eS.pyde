def setup():
    size(600,600)
    stroke(255)
    noFill()
    
def draw():
    background(0)
    stroke(0,255,0)
    line(0,0,600,600)
    forme_bizarre(300,300,200)
    forme_bizarre(150,150,100)
    forme_bizarre(450,150,100)
    forme_bizarre(150,450,100)
    forme_bizarre(450,450,100)
    forme_bizarre(mouseX,mouseY,50)
    
    
    
# Je crée mon outil forme_bizarre
# x : abscisse où faire le dessin
# y : ordonnée où faire le dessin
# fat : taille du dessin
# Note : pour tout plainte concernant le nom des variables, contacter Gaëtan
def forme_bizarre(x,y,fat):
    stroke(255)
    circle(x,y,fat)
    ellipse(x,y,fat,fat/2)
    ellipse(x,y,fat/2,fat)
    stroke(255,0,0)
    circle(x,y,fat/2)
