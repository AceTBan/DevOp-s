def setup():
  size(950,1000)
  background(0)
  stroke(255)
  strokeWeight(5)



def draw():
  print (mouseX,mouseY)



def mouseClicked():
    noFill()
    circle(mouseX,mouseY,50)
