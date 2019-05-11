from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from .mover import Mover
from .plant import Plant
from .trail import Trail

import numpy as np
import json
import atexit
import os

from paths.parse_trails import imageParser

class Model(Model):
    def __init__(self, n_movers, n_plants, width, height, snippet_length):

        # define settings
        self.grid = MultiGrid(width, height, False)
        self.schedule  = RandomActivation(self)

        self.call_counter = 0

        # register parsing at sim exit
        parser = imageParser(n_movers)
        atexit.register(parser.write_poems)


        # place agents on the grid
        for i in range(n_movers):
            pos = (np.random.randint(width),np.random.randint(height))
            baby = Mover(pos, self, i)
            self.schedule.add(baby)
            self.grid.place_agent(baby, pos)

        # place plants on the grid
        source_list = [n for n in os.listdir("corpus") if n!=".DS_Store"]
        start = {source:0 for source in source_list} # counting array needs to be outside loop

        for i in range(n_plants):
            # step through text sources
            # alternate sources every time
            source = source_list[i%len(source_list)]
            text_start = start[source]
            start[source] += snippet_length
            # print("%s: %s"%(source, start[source]))

            pos = (np.random.randint(width),np.random.randint(height))
            growth = Plant(pos, self, text_start, source, snippet_length)
            self.schedule.add(growth)
            self.grid.place_agent(growth, pos)

        # set flag for mesa
        self.running = True

    def step(self):
        self.schedule.step()

    # function that gets called from mover to add a trail to the map
    def add_trail(self, marker_pos, origin, agent):
        # make a trail_marker
        trail_marker = Trail(marker_pos, self, origin, agent)

        # add to the grid
        self.grid.place_agent(trail_marker, marker_pos)
        self.call_counter +=1

    def remove_trail(self, trail_instance):
        self.grid.remove_agent(trail_instance)
