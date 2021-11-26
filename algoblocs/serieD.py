from turtle import *

current_color = 0
def shift_color(n):
    global current_color
    current_color += n
    current_color %= 1
    t = [(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(1,0,0)]
    n1 = int(6*current_color)
    n2 = n1+1
    w1 = 6*current_color-n1
    w2 = 1-w1
    color(t[n1][0]*w2+t[n2][0]*w1,t[n1][1]*w2+t[n2][1]*w1,t[n1][2]*w2+t[n2][2]*w1)

# D-1 : Stop

# D-2 : Serpentin

# D-3 : Z

# D-4 Escalier biscornu

# D-5 : Allumette

# D-6 : Longueur variable

# D-7 : Interrogation

# D-8 : 































































# D6
#longueur = 100
#fd(longueur)
#seth(270)
#longueur = 200
#fd(longueur)
#seth(0)
#longueur = 300
#fd(longueur)

# D7
#longueur = 100
#seth(90)
#fd(longueur)
#seth(0)
#fd(longueur)
#seth(90)
#longueur = 200
#fd(longueur)
#seth(180)
#fd(longueur)
#longueur = 100
#seth(270)
#fd(longueur)

# D9

# longueur = 100
# for _ in range(20):
#     fd(longueur)
#     right(120)
#     # longueur = longueur+40
#     longueur += 40



































































input()    