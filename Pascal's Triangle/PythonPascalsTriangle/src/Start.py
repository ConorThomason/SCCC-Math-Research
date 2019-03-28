from PascalTree import PascalTree
from GraphGenerator import GraphGenerator
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import holoviews as hv

from holoviews import opts

tree = PascalTree(20)		
#At this point, the outerlying labels have been established.
generator = GraphGenerator(tree)

hv.extension('matplotlib')

#nx.draw_networkx(generator.getGraph(), generator.getPos(), labels=generator.getLabels(), with_labels=True)
nx.draw_networkx(generator.getGraph(), generator.getPos(), labels=generator.getLabels(), with_labels=True)
#n = Network(height = 800, width = 800, notebook = True)
#n.from_nx(generator.getGraph())
#n.toggle_physics(False)
#n.show("ex.html")
finalGraph = generator.getGraph()
graph = hv.Graph.from_networkx(finalGraph, generator.getPos())

%%opts Distribution [width=600 height=400]

#(graph * labels.opts(text_font_size='8pt', text_color='white', bgcolor='gray'))

renderer = hv.renderer('bokeh')

renderer.save(graph, 'graph')

plot = renderer.get_plot(graph).state

hv.Graph.from_networkx(generator.getGraph(), generator.getPos())
plt.axis('off') #Required to remove axis, don't know why savefig doesn't do it.
plt.tight_layout()
plt.savefig("path.png", axis=False)
tree.printTree()
#app = Viewer(generator.getGraph())
#app.mainloop()
print("Complete")
