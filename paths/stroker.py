

from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve
import numpy as np

def gen_random_points(l):
    ##generate some tuples of points constrained by a 10 by 10 grid
    points = [(np.random.poisson(), np.random.poisson()) for n in range(l)]

    return points


def path_from_points(points):
    pathlist = []
    for i,p in enumerate(points):
        # beginning
        if i==0:
            pathlist.append(beginknot(*p))
            pathlist.append(tensioncurve())
            # print("beginknot(*points[%s])"%i)
            # print("tensioncurve()")

        # end
        elif i==len(points)-1:
            pathlist.append(endknot(*p))
            # print("endknot(*points[%s])"%i)

        # middle
        else:
            # print("smoothknot(*points[%s])"%i)
            # print("tensioncurve()")
            pathlist.append(smoothknot(*p))
            pathlist.append(tensioncurve())

    path = metapost.path.path(pathlist)

    return path
