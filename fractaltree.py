#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from graph_objs import *
from math import pi as PI
from math import sin, cos
import random
root=0

# just testing commit.
def fractal_tree(iterat, origin, t, r, theta, dtheta, root_col, tip_col):
    """
    draws branches
    iterat:     iteratation number, stop when iterat == 0
    origin:   x,y coordinates of the start of this branch
    t:        current trunk length
    r:        factor to contract the trunk each iteratation
    theta:    starting orientation
    dtheta:   angle of the branch
    """
    if iterat == 0:
        return
    # render the branch
    x0, y0 = origin
    x, y = x0 + t * cos(theta), y0 - t * sin(theta)
    # color the branch according to its position in the tree
    col = get_col(root_col, tip_col, iterat)
    # add to traces
    lines.append(Scatter(x=[x0, x], y=[y0, y], line=Line(color=col)))
    # recursive calls
    fractal_tree(iterat-1, (x,y), t * r, r, theta + dtheta, dtheta, root_col, tip_col)
    fractal_tree(iterat-1, (x,y), t * r, r, theta - dtheta, dtheta, root_col, tip_col)

# color the tree with a gradient from root_col to tip_col
# interpolate linearly to get color at a given position in the gradient
def get_col(root_col, tip_col, iterat):
    r = ((iterat*1.0/root)*(root_col[0]-tip_col[0]))+tip_col[0]
    g = ((iterat*1.0/root)*(root_col[1]-tip_col[1]))+tip_col[1]
    b = ((iterat*1.0/root)*(root_col[2]-tip_col[2]))+tip_col[2]
    return '#%02x%02x%02x' % (r,g,b)


if __name__ == '__main__':
    # angle to radian factor
    ang2rad = PI/180.0
    # experiment with number of iteratations (try 4 to 14)
    iterat = 12
    # experiment with trunk length (try 120)
    t = 120
    # experiment with factor to contract the trunk each iteratation (try 0.7)
    r = 0.7
    # starting orientation (initial 90 deg)
    theta = 90.0 * ang2rad
    # experiment with angle of the branch (try 18 deg)
    dtheta = 18.0 * ang2rad
    # experiment with gradient color choices
    root_col = (40,40,40)
    tip_col = (250,250,250)
    # center of bottom
    origin = (250, 500)
    root=iterat
    # make the tree
    lines = []
    fractal_tree(lines, iterat, origin, t, r, theta, dtheta, root_col, tip_col)

