'''
This file is created to make art as well as generating the Recaman Sequence.
'''

from numpy import cos,sin,arccos
import numpy as np
from pylab import *

def parametric_circle(t,xc,yc,R):
    x = xc + R*cos(t)
    y = yc + R*sin(t)
    return x,y

def inv_parametric_circle(x,xc,R):
    t = arccos((x-xc)/R)
    return t

def create_circle_def(x1, x2):
    R = abs(x2-x1)/2
    xc = max(x1,x2) - R
    return R, xc, 0

def generate_recaman(n):
    rs = [0]

    for i in range(1,n):
        n_ut = rs[i-1] - i
        if  n_ut > 0 and n_ut not in rs:
            rs.append(n_ut)
        else:
            rs.append(rs[i-1] + i)
    return rs

def cross_sum(n:int) -> int:
    result = n
    while result > 9:
        result = sum(list(map(int,str(result))))
    return result

def Show_recaman(n):
    colors = ["yellow", "blue", "red"]
    N = 100
    data = generate_recaman(n)
    for i in range(len(data)-1):
        start_point = data[i]
        end_point = data[i+1]
        R, xc, yc = create_circle_def(start_point, end_point)
        color_index = cross_sum(i) % 3
        start_t = inv_parametric_circle(start_point, xc, R)
        end_t   = inv_parametric_circle(end_point, xc, R)
        if i % 2 == 0:
            arc_T = -1 * np.linspace(start_t, end_t, N)
        else:
            arc_T = np.linspace(start_t, end_t, N)

        X,Y = parametric_circle(arc_T, xc, yc, R)
        plot(X,Y, color=colors[color_index])
        scatter(X,Y ,s=0)
        axis('equal')

    show()


Show_recaman(57-1)