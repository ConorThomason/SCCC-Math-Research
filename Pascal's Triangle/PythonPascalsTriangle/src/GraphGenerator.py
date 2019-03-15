import networkx as nx
import matplotlib.pyplot as plt
class GraphGenerator:
    G = nx.Graph()
    labels = []
    nodeCount = 0
    def generateNodes(self, tree):    
        for i in range(tree.getRowCount()):
            values = tree.getRow(i)
            for j in range(values):
                G.add_node(nodeCount)
                nodeCount = nodeCount + 1
        labels.append(values)
    def getGraph(self):
	    return self.G