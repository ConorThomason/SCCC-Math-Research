from PascalTree import PascalTree
from GraphGenerator import GraphGenerator
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import holoviews as hv

tree = PascalTree(10)		
#At this point, the outerlying labels have been established.
generator = GraphGenerator(tree)


#nx.draw_networkx(generator.getGraph(), generator.getPos(), labels=generator.getLabels(), with_labels=True)
nx.draw_networkx(generator.getGraph(), generator.getPos(), labels=generator.getLabels(), with_labels=True)
#n = Network(height = 800, width = 800, notebook = True)
#n.from_nx(generator.getGraph())
#n.toggle_physics(False)
#n.show("ex.html")
graph = hv.Graph.from_networkx(generator.getGraph(), generator.getPos())
#labels = hv.Labels(graph.nodes, ['x','y'], generator.getLabels())
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


#Current issues:
#Node has no position - Node count is going to 65?
#Labels aren't generating properly (all 1s)