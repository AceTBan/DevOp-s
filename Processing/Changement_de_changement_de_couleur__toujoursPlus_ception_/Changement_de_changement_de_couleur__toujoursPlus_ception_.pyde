def setup():
  size(950,1000)
  background(0)
  stroke(255)
  strokeWeight(5)
  noFill()
  global c
  c = 0
  global mode
  mode=0




def draw():
  print (mouseX,mouseY)
  background(0)
  global c
  c= (c+1)%256
  
  if mouseY<500:
      square(450-mouseX/2,500-mouseX/2,mouseX)
  elif mouseY>500:
    circle(450,500,mouseX)
    
    if mode == 0:
        fill(c,0,0)
    elif mode == 1:
        fill(0,c,0)
    else:
        fill(0,0,c)
    
def mouseClicked():
    global mode
    mode = (mode+1)%3
