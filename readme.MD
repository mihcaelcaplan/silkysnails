## Explanation

The project started with this abstract:
> I want to create digital silkworms that live inside an agent-based modelling framework called [Mesa](https://mesa.readthedocs.io/en/master/). Agent-based modelling frameworks are commonly used to study emergent properties of multi-agent interactions, like bird or fish flocking behavior. Programmatically, I will create a poetic digital terrain that the agents will navigate, based on some sort of lifelike incentives. As they navigate, each agent will leave behind a textual trace, analogous to a snail-trail or silk fiber. This trail of words could be followed by other agents, or woven into some fabric by the interactions with other digital agents. At the end of a simulation, I will have a two dimensional web of overlapping text, laid down by the agents.

I worked in an agent-based simulation framework called [Mesa](https://mesa.readthedocs.io/en/master/) to instantiate agents (I am in the habit of referring to them as silksnails) and to give them a simple environment to navigate in. The environment consists of a two dimensional grid populated with static “plants” that represent sources of text. When the agents come into contact with these plants, they eat and fill their bellies with text. The plant is now empty for them, and they continue to move around the environment in search for more food. As they move, they lay down text that becomes associated with the two-dimensional coordinates that they pass through. Each other agent in the simulation will follow a trail that they encounter with reverse polarity, away from the agent that is the source of the trail, and toward the plant from which the trail must have originated. After the simulation has finished, the trails of text that the agents have left behind are parsed into smooth paths of text and a PDF is generated that shows the paths of each agent through space.

## How to read the code

The interesting parts of the code live inside the "simulation" folder. These define the rules of the simulation. The silksnails are defined inside the file `mover.py`, the plants in `plant.py` and `trail.py` is a very short file that is used to lay a trail in the simulation. `model.py` defines the system-level configuration of the simulation, and `server.py` is used to link the Python code with the visualization which runs in a web browser.

`mover.py` is the most engaging read, and offers some insight into how the agents navigate their world.


## Using this software

First, you must set up your programming environment correctly. I didn’t have time to compile everything into a nice executable, so running the source code is your only option to programmatically interact with this world and to generate your own poems.

You must have a working Python installation, preferably version 3.4 - 3.6. I think 3.7 breaks [Mesa](https://mesa.readthedocs.io/en/master/), and I had to downgrade at the start of the project.

Once your Python installation is set up, you must install [PyX](http://pyx.sourceforge.net/), which handles the PDF generation using a TeX backend. The installation instructions for [PyX](http://pyx.sourceforge.net/) are here: http://pyx.sourceforge.net/manual/index.html. You must separately install TeX, instructions for which can be found here: https://www.latex-project.org/get/.

Once you have done this, install [Mesa](https://mesa.readthedocs.io/en/master/) using the instructions here: https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html.

Then, you’re ready to go!

Download this repository as a .zip file or as a GIT repository using the command line, instructions for which can be found here: https://help.github.com/en/articles/cloning-a-repository.
Simply run the file named "run.py" using the command `python run.py` in your terminal after navigating to the working directory. A browser window will open, and you will be able to set some parameters before running the simulation using the “Start” button in the menu bar. When you are finished with the simulation, inputting the key-combination `Ctrl+C` in the terminal window will stop the process and generate the image output.

## Media

A screen capture of the simulation process:


Some examples of generated poems, and shots of the corresponding simulation windows:
Poem 1:
<object data="https://github.com/mihcaelcaplan/silkysnails/raw/master/media/1/full.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/mihcaelcaplan/silkysnails/raw/master/media/1/full.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/mihcaelcaplan/silkysnails/raw/master/media/1/full.pdf">Download PDF</a>.</p>
    </embed>
</object>


## Statement

To structure the movement of the agents through the environment, I drew on Lucretius’ notion of clinamen, the random swerve of atoms through space from which the world derives its substance. When the silksnails are born, they start to move randomly, until they are near enough to a plant that they can sense it. They are buffeted by invisible forces, generated by random choices of (x,y) coordinate pairs, until they are able to nourish themselves. Through this decision, I made the choice to transpose a metaphysical concept meant to apply on a microscopic scale to the digital-macroscopic scale of the simulation. When they are within distance, they move towards the plant and feed on the text that lies within. This feeding process is purely linguistic, the creatures engorging themselves on text which is held within their abstract and limitless stomachs (referred to as self.belly throughout the code). A full silksnail (len(self.belly) > 0) will lay it’s trail down upon each square of the grid through which it moves. When the belly is empty, the trail runs out. It is entirely possible for some agents to never find food throughout the course of the simulation, and correspondingly to lack any poetic output. In contrast, some agents may never go hungry, laying a trail that forms a record of their entire lifespan.

The plants are created by chopping up my source texts into small chunks that can be easily digested by the hungry creatures. As sources, I have chosen three texts, all of them drawn from the material that we engaged with throughout the course of the class. The raw text that the plants are built from can be found in the “corpus” folder.

First, I chose an excerpt of the first chapter of Jane Bennett’s *Vibrant Matter*, “The Force of Things.” I chose this text because I enjoyed reading it, and because the themes with which it engages are relevant to this project. Throughout the chapter, Bennett seeks to engage with the life-force of things that fall outside of the typical categories that people associate with life. In building this digital world of abstract creatures and poetic creation, I desired to engage with the ways in which digital technology and culture fall in grey areas, somewhere between inanimacy and animacy. The framework that I used is designed for agent-based modeling, a technique which instantiates large numbers of agents, each with simple rules that mediate their interactions with the digital environment. Through their interactions, large scale patterns can be observed. The technique is an alternative to standard modelling with differential equations, mostly chosen in situations where people are not satisfied with tracking statistical averages, and want to see these patterns emerge from discrete interactions (a good explanation of the high-level differences can be found here: http://systems-sciences.uni-graz.at/etextbook/sysmod/ebm_vs_abm.html). What category do these agents fall into? They are derived from abstractions layered on top of abstractions, perhaps most fundamentally existing as electrons undergoing transport through tightly manufactured semiconductive materials whose properties can be exploited to instantiate systems of boolean logic and subsequently, arithmetic. But, in some sense, they are alive. They make decisions and interact with their environment. It is common in simple simulations of emergent properties to model flock or swarm behaviors by instantiating agents with three simple rules that cause visually intelligible swarm behavior to appear (full explanation of the pioneering work can be found here: https://en.wikipedia.org/wiki/Boids). Equipped with the philosophical background that can be found in the Bennett reading, it is impossible not to wonder about the status of these digitally lifelike entities.

I also chose an excerpt from “Snails and their Trails,” which motivated my addition of trail following behavior in the simulation. This is only way that the silksnails interact with their brethren, and it should cause spatial-textual patterns to emerge that otherwise would be absent. The discussion of trail following in this work is highly detailed, and scientifically complex. This detail is lacking in my simulation, as code complexity scales non-linearly with the amount of small details that need to be added. Crucially, the researchers discuss the polarity of snail-trails, and this is something that I added. The motivations for gastropod trail following are complex and not particularly well understood. They seem to vary across species and environmental context. In the context of my simulation, I chose trail following to be a mechanism for finding food sources. For this reason, the silksnails follow the reverse polarity of the trail, away from the agent which has laid it down.

Finally, I excerpted the poetry from *Silk Poems*, by Jen Bervin. Her work engages meaningfully with life forms that, as living beings, are often overlooked as small and insignificant but, as production mechanisms, are historically important as unique sources of sought-after cloth. The book artistically interprets the lifeworld of silkworms as members of a class of organisms, and as individual living beings. In addition, Bervin seriously engaged with the materiality of silk as a material, and ultimately wrote a poem in silk that must be viewed under a microscope. This work motivated the project, giving me the idea to lay textual traces as poetic encodings of digital-lifeforms.

The poems emerge as properties of a self-contained digital world, created by the interactions of abstracted lifeforms with their simple environment. They are visually interesting, following long arcs across space, often punctuated by tight loops formed by random movement in a small radius. The text itself is only sometimes legible, becoming obscured as it crosses its own trail as well as those of the other agents. Sometimes it is upside down, sideways, or in other unreadable positions. It is the story of each small silksnail.
