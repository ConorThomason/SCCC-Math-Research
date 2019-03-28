import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import holoviews as hv
import csv
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
from PascalTreeIterator import PascalTreeIterator
class GraphGenerator:
    iterator = None
    G = None
    labels = {}
    labelTable = None
    pos = {}
    posX = []
    posY = []
    nodeCount = 0
    def __init__(self, tree):
        self.iterator = PascalTreeIterator(tree)
        self.G = nx.MultiDiGraph()
        self.generatePos(tree)
        self.generateNodes(tree)
        self.generateEdges(tree)
        self.generateNodeLabels(tree)
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
        with open('edges.csv', 'w', newline='') as csvfile:
            fieldNames = ['from', 'to']
            writer = csv.DictWriter(csvfile, fieldnames = fieldNames)
            writer.writeheader()
            for i in range(tree.getRowCount() - 1):
                for j in range(i):
                    self.G.add_edges_from([(currentNode, currentNode + i), (currentNode, currentNode + i + 1)])
                    writer.writerow({'from': currentNode, 'to': currentNode + i})
                    writer.writerow({'from': currentNode, 'to': currentNode + i + 1})
                    currentNode = currentNode + 1
                
    def generateNodeLabels(self, tree):
        with open('nodes.csv', 'w', newline='') as csvfile:
            fieldNames = ['id', 'value', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames = fieldNames)
            writer.writeheader()
            for i in range(tree.getNodeCount()):
                labelString = str(self.iterator.getCurrentNode().get_value())
                writer.writerow({'id': i, 'value': self.iterator.getCurrentNode().get_value(), 'x': self.posX[i], 'y': self.posY[i]})
                self.labels[i] = labelString
                self.iterator.orderedNextNode()
                
            print(self.labels)
        self.labelTable = hv.Table(self.labels)
    def getLabelTable(self):
        return self.labelTable
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
                self.posX.append(currentX)
                self.posY.append(currentY)
                currentNode = currentNode + 1
                currentX = currentX - 10
            currentY = currentY + 5
            baseX = baseX + 5
        print(self.pos)
    def getPos(self):
        return self.pos