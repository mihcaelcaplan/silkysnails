from mesa import Agent
import re
import numpy as np
import io

class Plant(Agent):
    # this will be the main lil organism

    def __init__(self, pos, model, text_start, source_name, length):

        super().__init__(pos, model)
        # print(pos)
        self.x, self.y = pos
        self.text_start = text_start
        self.source_name = source_name
        self.source = self.get_text_source(length)

        if not self.source:
            print("Warning! Plant instantiated with no text. Source %s seems to be too short for the number of agents."%source_name)



    #will get called in the __init__ to assign text to plant
    def get_text_source(self, length):
        # open a .txt file and pick some substring of complete words

        with io.open("corpus/%s"%self.source_name, 'r', encoding='windows-1252') as f:
            print("opening: corpus/%s"%self.source_name)

            list = re.split('\W+', f.read())

        #randomly subselect some section of the list
        x = np.random.randint(0, len(list))
        source = list[self.text_start:self.text_start+length]
        # print(source)

        return source
