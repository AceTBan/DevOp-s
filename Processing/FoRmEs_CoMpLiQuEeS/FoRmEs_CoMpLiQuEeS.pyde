def setup():
  size(950,1000)
  background(0)
  stroke(255)
  strokeWeight(5)
  noFill()
  
def draw():
  print (mouseX,mouseY)
  background(0)

  circle(450,500,200)
  circle(450,500,100)
  ellipse(450,500,200,100)
  ellipse(450,500,100,200)
  
  circle(150,150,200)
  circle(150,150,100)
  ellipse(150,150,200,100)
  ellipse(150,150,100,200)

  circle(800,800,200)
  circle(800,800,100)
  ellipse(800,800,200,100)
  ellipse(800,800,100,200)
  
  circle(800,150,200)
  circle(800,150,100)
  ellipse(800,150,200,100)
  ellipse(800,150,100,200)
  
  circle(150,800,200)
  circle(150,800,100)
  ellipse(150,800,200,100)
  ellipse(150,800,100,200)
  
  circle(mouseX,mouseY,100)
  circle(mouseX,mouseY,50)
  ellipse(mouseX,mouseY,100,50)
  ellipse(mouseX,mouseY,50,100)
