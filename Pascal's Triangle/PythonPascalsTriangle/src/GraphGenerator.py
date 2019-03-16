import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
from PascalTreeIterator import PascalTreeIterator
class GraphGenerator:
    iterator = None
    G = None
    labels = {}
    pos = {}
    nodeCount = 0
    def __init__(self, tree):
        self.iterator = PascalTreeIterator(tree)
        self.G = nx.MultiDiGraph()
        self.generateNodes(tree)
        self.generateEdges(tree)
        self.generateNodeLabels(tree)
        self.generatePos(tree)
    def getGraph(self):
	    return self.G
    
    def getLabels(self):
        return self.labels
    
    def generateNodes(self, tree):
        self.G.add_nodes_from(range(tree.getNodeCount()))
    
    def generateEdges(self, tree):
        currentNode = 0
        currentRow = 1
        for i in range(tree.getRowCount()):
            for __ in range(i):
                self.G.add_edges_from([(currentNode, currentNode + i), (currentNode, currentNode + i + 1)])
                currentNode = currentNode + 1
    
    def generateNodeLabels(self, tree):
        for i in range(tree.getNodeCount()):
            labelString = str(self.iterator.getCurrentNode().get_value())
            self.labels[i] = labelString
            self.iterator.orderedNextNode()
    
    def getLabels(self):
        return self.labels
    
    def generatePos(self, tree):
        currentNode = 0
        currentX = 0
        currentY = 0
        for i in range(tree.getRowCount()):
            for __ in range(i):
                self.pos[currentNode] = (currentX, currentY)
                currentNode = currentNode + 1
                currentX = currentX - 1
                currentY = currentY - 1
                
    def getPos(self):
        return self.pos