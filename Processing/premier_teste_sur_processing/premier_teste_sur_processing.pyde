def setup():
  size(950,1000)
  background(255,144,0)
  stroke(123,147,159)
  noFill()


def draw():
  print (mouseX,mouseY)
  square(200,10,200)
  line(100,300,500,50)
  circle(mouseX,mouseY,123)
  circle(mouseX,mouseY,50)
  square(mouseY,mouseX,50)
  line(mouseX,mouseY,425,0)


def mouseClicked():
    line(mouseX,mouseY,422,0)
    circle(200,10,200)
    square(100,50,20)
