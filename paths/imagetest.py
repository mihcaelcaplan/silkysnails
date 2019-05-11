from paths.stroker import *

# get a path from points
points = gen_random_points(100)
p = path_from_points(points)

# # get some text
with open("corpus/1.txt","r") as f:
    text = f.read().replace('\n', ' ')

# set up canvas and draw text
c = canvas.canvas()
c.draw(p, [deco.curvedtext(text)])

# c.writeEPSfile("textalongpath")
c.writePDFfile("textalongpath")
# c.writeSVGfile("textalongpath")
