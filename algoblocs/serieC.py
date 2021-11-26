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

# C-1 : Dents

# for _ in range(100):
#     setpos(0,0)
#     clear()
#     for _ in range(4):
#         for _ in range(3):
#             fd(100)
#             left(-120)
#         fd(100)

# C-2 : Fenêtres

# seth(90)
# for _ in range(5):
#     for _ in range(4):
#         fd(100)
#         right(90)
#     up()
#     fd(200)
#     down()

# C-3 : Couleurs décalées

# shift_color(0.33)
# for _ in range(3):
#     for _ in range(8):
#         fd(200)
#         left(180-45)
#     up()
#     shift_color(0.1)
#     fd(400)
#     down()

# C-4 : Pâté de maisons

# for _ in range(6):
#     color('red')
#     for _ in range(3):
#         fd(100)
#         left(180-60)
#     color('orange')
#     for _ in range(4):
#         fd(100)
#         right(90)
#     up()
#     fd(200)
#     down()

# C-5 : Quadriétoile

# shift_color(0.8)
# for _ in range(8):
#     for _ in range(8):
#         fd(400)
#         left(180-45)
#     shift_color(0.25)
#     right(90)

# C-6 : Triangle doré

# for _ in range(3):
#     for _ in range(7):
#         fd(200)
#         left(180-60)
#     fd(200)

# C-7 : Soleil

# for _ in range(8):
#     fd(100)
#     left(180-135)
#     for _ in range(3):
#         fd(100)
#         left(180-300)

# C-8 : Fleur

# seth(90)
# fd(400)
# left(180-135)
# for _ in range(4):
#     for _ in range(3):
#         color('red')
#         fd(200)
#         left(180-60)
#     color('yellow')
#     fd(200)
#     right(90)

# C-9 : Triboucle

# for _ in range(3):
#     for _ in range(3):
#         fd(100)
#         right(180-60)
#         for _ in range(4):
#             right(90)
#             fd(100)
#     left(180-60)
#     fd(400)

# C-10 : Empilement

# seth(-90)
# for _ in range(4):
#     for _ in range(4):
#         fd(100)
#         for _ in range(4):
#             left(90)
#             fd(50)
#         right(90)
#     fd(200)

# C-11 : multihexagone

# shift_color(0.5)
# for _ in range(6):
#     for _ in range(6):
#         for _ in range(3):
#             fd(100)
#             left(180-60)
#         fd(100)
#         left(180-120)
#     up()
#     fd(200)
#     shift_color(0.1)
#     left(180-240)
#     down()

# C-12 : Soleil & Lune

for _ in range(2):
    for _ in range(2):
        for _ in range(2):
            circle(100,90)
            fd(100)
            left(90)
    circle(100,45)
# color('blue')
# circle(100,90)
# circle(100,90)
# left(180-60)
# circle(200,300)




input()