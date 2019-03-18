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
        print(self.G.nodes)
    
    def generateEdges(self, tree):
        currentNode = 0
        currentRow = 1
        for i in range(tree.getRowCount() - 1):
            for j in range(i):
                self.G.add_edges_from([(currentNode, currentNode + i), (currentNode, currentNode + i + 1)])
                currentNode = currentNode + 1
    def generateNodeLabels(self, tree):
        for i in range(tree.getNodeCount()):
            labelString = str(self.iterator.getCurrentNode().get_value())
            self.labels[i] = labelString
            self.iterator.orderedNextNode()
        print(self.labels)
    def getLabels(self):
        return self.labels
    
    def generatePos(self, tree):
        scaleFactor = tree.getNodeCount()
        currentNode = 0
        currentRowCount = 1
        baseX = 0
        currentX = 0
        currentY = 0
        for i in range(tree.getRowCount()):
            currentX = baseX
            for j in range(i):
                self.pos[currentNode] = (currentX, currentY)
                currentNode = currentNode + 1
                currentX = currentX + 10
            currentY = currentY - 5
            baseX = baseX - 5 
        print(self.pos)
        
    def getPos(self):
        return self.pos