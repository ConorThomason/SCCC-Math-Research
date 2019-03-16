from PascalTree import PascalTree
from GraphGenerator import GraphGenerator
import networkx as nx
import matplotlib.pyplot as plt

tree = PascalTree(10)		
#At this point, the outerlying labels have been established.
generator = GraphGenerator(tree)

# 
nx.draw(generator.getGraph(), generator.getPos(), labels=generator.getLabels(), with_labels=True)
plt.axis('off') #Required to remove axis, don't know why savefig doesn't do it.
plt.savefig("path.png", axis=False)
tree.printTree()
print("Complete")


#Current issue - Node has no position. Likely either due to the node creation process (May be creating too many, but unlikely)
# or it is in relation to how the positions themselves are assigned.