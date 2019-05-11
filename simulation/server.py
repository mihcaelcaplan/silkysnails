from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from .model import Model
from .mover import Mover
from .plant import Plant
from .trail import Trail
from mesa.visualization.UserParam import UserSettableParameter


# portrayal funcs for everyone
def portrayal(inhabitant):
    assert inhabitant is not None

    if type(inhabitant) is Mover:
        portrayal =  {
            "Shape": "rect",
            "w": 1,
            "h": 1,
            "Filled": "true",
            "Layer": 2,
            "x": inhabitant.x,
            "y": inhabitant.y,
            "Color": "black"
        }
    elif type(inhabitant) is Trail:
        portrayal =  {
            "Shape": "rect",
            "w": 1,
            "h": 1,
            "Filled": "true",
            "Layer": 0,
            "x": inhabitant.x,
            "y": inhabitant.y,
            "Color": "grey"
            }
    elif type(inhabitant) is Plant:
        portrayal =  {
            "Shape": "circle",
            "r": 1,
            "Filled": "true",
            "Layer": 1,
            "x": inhabitant.x,
            "y": inhabitant.y,
            "Color": "green"
        }


    return portrayal


# make some params user settable
n_agent_slider = UserSettableParameter('slider', "Number of Agents", 5, 1, 25, 1)
n_plant_slider = UserSettableParameter('slider', "Number of Plants", 50, 1, 1000, 1)


params = {'n_movers':n_agent_slider,
          'n_plants':n_plant_slider,
          'width':20,
          'height':20,
          'snippet_length': 20
}

display_width = 500
display_height = 500
canvas_element = CanvasGrid(portrayal, params['width'], params['height'], display_width, display_height)


server = ModularServer(Model, [canvas_element], "Silky", params)
