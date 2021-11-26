def setup():
  size(950,1000)
  background(0)
  stroke(255)
  strokeWeight(1)



def draw():
  print (mouseX,mouseY)
  noFill()
  circle(mouseX,mouseY,50)
