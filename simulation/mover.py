from mesa import Agent
import numpy as np
from .plant import Plant
from .trail import Trail

import atexit
import json


class Mover(Agent):
    # this will be the main lil organism

    def __init__(self, pos, model, unique_id):
        super().__init__(pos, model)
        # print(pos)
        self.x, self.y = pos
        self.id = unique_id
        self.belly = []
        self.trail = []
        self.visited_plants = []
        self.last_pos = ()


    def step(self):
        print(self.id)
        # eat if appropriate
        self.handle_plants()

        # save last pos b4 movement
        self.last_pos = self.pos

        # move
        self.move()

        # lay the trail
        if len(self.belly)>0:
            self.lay_trail(self.last_pos)

        #at end of each step, update the trail in json, unfortunately the atexit method
        # doesn't work because garbage collection eats the trail array b4 it outputs
        self.output_json()

    # move handler
    def move(self):

        # check if near plants or on trail
        near_plant, plants = self.near_plant()
        on_trail, trail_elements = self.on_trail()

        # flow
        if near_plant:
            for plant in plants:
                if plant not in self.visited_plants:
                    self.model.grid.move_agent(self, plant.pos)
                    print("moving to plant")
                    return
                else:
                    self.move_random(exclude=[n.pos for n in plants])
                    print("moving randomly with exclusion")
                    return

        if on_trail:
            for trail in trail_elements:
                if trail.agent != self:
                    self.follow_trail(trail)
                    print("following trail")
                    return
                else:
                    print("passing to random")
                    pass

        # if haven't returned
        print("moving randomly")
        self.move_random()


# generic random_move function stolen from wolf_and_sheep mesa example
    def move_random(self, exclude=None):

        if not exclude:
            # Pick the next cell from the adjacent cells.
            next_moves =self.model.grid.get_neighborhood(self.pos, True)
            idx = np.random.choice(len(next_moves))
            next = next_moves[idx]
        else:
            next_moves = [n for n in self.model.grid.get_neighborhood(self.pos, True) if n not in exclude]
            idx = np.random.choice(len(next_moves))
            next = next_moves[idx]

        self.model.grid.move_agent(self, next)

    def near_plant(self):
        plant_list = []
        for cell in self.model.grid.get_neighborhood(self.pos, True):
            for n in self.model.grid.get_cell_list_contents(cell):
                if type(n)==Plant:
                    plant_list.append(n)
        if plant_list:
            return (True, plant_list)
        else:
            return(False, None)

    def on_trail(self):
        # check for trail elements
        trail_elements = []
        for n in self.model.grid.get_cell_list_contents(self.pos):
            if type(n)==Trail:
                trail_elements.append(n)

        # if on trail, return
        if trail_elements:
            return (True, trail_elements)
        else:
            return (False, None)


    def lay_trail(self, to):
        # get the first item in the word list
        word = self.belly.pop(0)

        # add a trail to the grid by calling model level place function
        self.model.add_trail(self.pos, self.last_pos, self)

        # add to the trail list
        self.trail.append((self.pos,word))


    def follow_trail(self, trail):
        print("trail following")
        self.model.grid.move_agent(self, trail.origin)
        # print("following a trail!")
        self.model.remove_trail(trail)


# check if the agent is on a source/plant
    def handle_plants(self):
        for n in self.model.grid.get_cell_list_contents(self.pos):
            if type(n) is Plant:
                # add text
                self.belly.extend(n.source)
                self.visited_plants.append(n)
                # print(self.visited_plants)

    # json output to run at the end
    def output_json(self):

        # construct an object
        output = {
            'name':self.id,
            'trail':self.trail

        # loop through each agent in the sim and construct a json output
        }
        with open("outputs/%s.json"%self.id,'w') as f:
            json.dump(output, f)
