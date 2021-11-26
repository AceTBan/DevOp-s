def setup():
  size(950,1000)
  background(0)
  stroke(255)
  strokeWeight(5)
  noFill()
  




def draw():
  print (mouseX,mouseY)
  background(0)
  
  if mouseY<500:
      square(450-mouseX/2,500-mouseX/2,mouseX)
  elif mouseY>500:
    circle(450,500,mouseX)
    
