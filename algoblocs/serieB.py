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

# B-1 : Escalier

# for _ in range(4) :
#     fd(50)
#     seth(270)
#     fd(50)
#     seth(0)

# B-2 : Créneaux

# for _ in range(4):
#     fd(100)
#     seth(0)
#     fd(100)
#     seth(270)
#     fd(100)
#     seth(0)
#     fd(100)
#     seth(90)

# B-3 : Carré

# for _ in range(4):
#     fd(200)
#     right(90)

# B-4 : Triangle

# for _ in range(3):
#     fd(200)
#     right(-120)

# B-5 : Drapeau

# seth(90)
# fd(200)
# color('red')
# for _ in range(3):
#     fd(100)
#     right(120)

# B-6 : Escalier bicolore

# for _ in range(2):
#     fd(100)
#     seth(90)
#     fd(100)
#     seth(0)
# for _ in range(3):
#     color('green')
#     fd(100)
#     seth(270)
#     fd(100)
#     seth(0)

# B-7 : Maison

# for _ in range(3):
#     fd(200)
#     left(120)
# for _ in range(4):
#     fd(200)
#     right(90)

# B-8 : Etoile

# for _ in range(8):
#     fd(400)
#     right(180-45)

# B-9 : Formes séparées

# fd(100)
# up()
# fd(100)
# down()
# for _ in range(3):
#     fd(200)
#     right(180-60)

# B-10 : Constellation

# for _ in range(8):
#     fd(200)
#     right(180-45)
# up()
# fd(400)
# down()
# color('yellow')
# for _ in range(8):
#     fd(400)
#     right(180)
#     right(45)
# up()
# color('pink')
# right(90)
# fd(200)
# down()
# for _ in range(8):
#     fd(200)
#     right(180-45)

# B-11 : Croix

# for _ in range(4):
#     fd(100)
#     left(90)
#     fd(100)
#     right(90)
#     fd(100)
#     right(90)

# B-12 : crochets

# for _ in range(3):
#     right(90)
#     fd(100)
# up()
# fd(100)
# color('green')
# down()
# for _ in range(3):
#     fd(100)
#     right(90)

# B-13 : 8 pattes

# for _ in range(8):
#     fd(100)
#     left(180-45)
#     fd(50)
#     right(90)
#     fd(50)
#     right(90)

# B-14 : Eclair

# for _ in range(8):
#     fd(100)
#     right(180-60)
#     fd(200)
#     left(180-60)
#     fd(100)

# B-15 : Carré arrondi

# for _ in range(6):
#     fd(200)
#     circle(100,90)

# B-16 Virages

# circle(400,90)
# seth(180)
# for _ in range(4):
#     circle(50,90)
#     circle(-50,90)

# B-17 : Flocon

# for _ in range(8):
#     circle(100,180)
#     left(180-60)

# B-18 : Encheêtrement

# for _ in range(8):
#     fd(400)
#     left(90)
#     fd(100)
#     left(180-135)

# B-19 : Frise ronde
# for _ in range(4):
#     circle(100,180)
#     seth(0)
# up()
# seth(90)
# fd(100)
# down()
# seth(180)
# for _ in range(4):
#     circle(100,180)
#     seth(180)

# B-20 : Photo

# seth(270)
# for _ in range(2):
#     fd(200)
#     circle(100,90)
# fd(100)
# for _ in range(2):
#     fd(200)
#     circle(100,90)
# fd(100)
# seth(0)
# fd(400)
# up()
# seth(270)
# fd(50)
# seth(180)
# fd(200)
# down()
# for _ in range(4):
#     circle(100,90)

# B-21 : Poissons

# for _ in range(6):
#     fd(200)
#     left(180-60)
#     fd(100)
#     left(180-60)
#     fd(200)
#     right(180-120)
#     fd(100)
#     right(180-60)
#     fd(100)
#     up()
#     right(180-60)
#     fd(200)
#     down()
#     shift_color(0.1)

# B-22 : Polygones réguliers

for _ in range(6):
    fd(200)
    left(180-120)
left(180-270)
for _ in range(6):
    color('red')
    fd(200)
    right(180-60)
color('green')
for _ in range(4):
    fd(200)
    left(90)
left(180-330)
for _ in range(4):
    fd(200)
    left(90)


































input()