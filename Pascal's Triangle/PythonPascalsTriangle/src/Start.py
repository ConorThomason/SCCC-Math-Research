from PascalTree import PascalTree
from GraphGenerator import GraphGenerator
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

tree = PascalTree(10)		
#At this point, the outerlying labels have been established.
generator = GraphGenerator(tree)


nx.draw_networkx(generator.getGraph(), generator.getPos(), labels=generator.getLabels(), with_labels=True)
n = Network(height = 800, width = 800, notebook = True)
n.from_nx(generator.getGraph())
n.toggle_physics(False)
n.show("ex.html")
plt.axis('off') #Required to remove axis, don't know why savefig doesn't do it.
plt.savefig("path.png", axis=False)
tree.printTree()
print("Complete")


#Current issues:
#Node has no position - Node count is going to 65?
#Labels aren't generating properly (all 1s)