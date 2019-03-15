from PascalTree import PascalTree
from GraphGenerator import GraphGenerator
import networkx as nx
import matplotlib.pyplot as plt

labels={}

tree = PascalTree(10)		
#At this point, the outerlying labels have been established.
generator = GraphGenerator()
generator.generateNodes(tree)

nx.draw(generator.getGraph())
plt.savefig("path.png")
tree.printTree()
print("Complete")
