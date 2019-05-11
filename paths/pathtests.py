from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve
import numpy as np

##generate some tuples of points constrained by a 10 by 10 grid
points = [(np.random.randint(-10,10), np.random.randint(-10,10)) for n in range(10000)]




pathlist = []
for i,p in enumerate(points):
    # beginning
    if i==0:
        pathlist.append(beginknot(*p))
        pathlist.append(tensioncurve())

    # end
    elif i==len(points)-1:
        pathlist.append(endknot(*p))

    # middle
    else:
        pathlist.append(smoothknot(*p))
        pathlist.append(tensioncurve())

path = metapost.path.path(pathlist)


c = canvas.canvas()
c.stroke(path)

# c.writeEPSfile("textalongpath")
c.writePDFfile("pathtest")
# c.writeSVGfile("textalongpath")
