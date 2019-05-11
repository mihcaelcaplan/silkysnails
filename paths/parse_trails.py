'''
This script should parse each .json in the ouputs directory and create a stroked path based on the trail
'''
import json
from paths.stroker import *
import os

class imageParser():

    def __init__(self, n_agents):
        self.n = n_agents
        self.data = {}


    def write_poems(self):
        self.get_data()
        self.write_full()


    def get_data(self):
        for i in range(self.n):
            print("Parsing agent #%s"%str(i))
        # grab the file, parse and delete
            with open("outputs/%s.json"%i,'r') as f:
                parsed = json.loads(f.read())
            os.remove("outputs/%s.json"%i)

            # make some lists and save them in the data_dict
            points = [tuple(n[0]) for n in parsed['trail']]
            text_list = [n[1] for n in parsed['trail']]
            self.data[i] = [points, text_list]


            print("\n")

    def write_full(self):
        # set up canvas
        c = canvas.canvas()

        for i in range(self.n):
            # try:
            if not self.data[i][1]:
                print("Warning: Agent #%s is empty!\n"%i)
            else:
                print("Adding Agent #%s to canvas"%i)
                print(self.data[i][1])
                text_string = ' '.join(self.data[i][1])
                print(text_string)

                # generate a path
                print("Building path...")
                p = path_from_points(self.data[i][0])

                print("Drawing path #%s out of %s"%(str(i+1), self.n))
                c.draw(p, [deco.curvedtext(text_string)])

            # except Exception as e:
                # print("\nwriting failed\n")
                # print(e)
                # print("Writing mysteriously failed for Agent #%s :("%i)

        print("Outputting PDF file...\n")
        c.writePDFfile("outputs/full")

    def write_individual(self):
        for i in range(self.n):
            try:
                if not self.data[i][1]:
                    print("Warning: Agent #%s is empty!\n"%i)
                else:
                    print("Writing poem for Agent #%s"%i)
                    print(self.data[i][1])
                    text_string = ' '.join(self.data[i][1])

                    # generate a path
                    print("Building path...")
                    p = path_from_points(self.data[i][0])

                    print("Drawing path...")
                    c = canvas.canvas()
                    c.draw(p, [deco.curvedtext(text_string)])

                    print("Outputting PDF file...\n")
                    c.writePDFfile("outputs/%s"%i)
            except:
                print("Writing mysteriously failed for Agent #%s :("%i)
