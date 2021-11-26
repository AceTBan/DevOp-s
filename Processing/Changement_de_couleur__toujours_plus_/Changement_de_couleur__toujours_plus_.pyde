def setup():
  size(950,1000)
  background(0)
  stroke(255)
  strokeWeight(5)
  noFill()
  global g
  g = 0




def draw():
  print (mouseX,mouseY)
  background(0)
  global g
  g= (g+1)%256
  fill(0,g,0)
  
  if mouseY<500:
      square(450-mouseX/2,500-mouseX/2,mouseX)
  elif mouseY>500:
    circle(450,500,mouseX)
    
