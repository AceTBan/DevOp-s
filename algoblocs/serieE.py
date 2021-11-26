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