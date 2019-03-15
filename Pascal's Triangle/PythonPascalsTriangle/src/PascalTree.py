from PascalNode import PascalNode
class PascalTree:
    rootNode = None
    rowCount = 1
    def __init__(self, value):
        self.rootNode = PascalNode(1)
        for i in range(value):
            self.generateNewRow()
            self.rowCount = self.rowCount + 1
            
    def generateNewRow(self):
        currentNode = self.rootNode
        secondRow = False
        if currentNode.get_next_left() == None:
            secondRow = True
        
        while currentNode.get_next_left() != None:
            currentNode = currentNode.get_next_left()
        
        currentNode.set_next_left(PascalNode(1))
        currentNode.get_next_left().set_previous_right(currentNode)
        
        if secondRow == False:
            while True:
                previousLeft = currentNode
                currentNode = currentNode.get_previous_right()
                currentNode = currentNode.get_next_right()
                currentNode.set_next_left(PascalNode(previousLeft.get_value() + currentNode.get_value()))
                
                currentNode.get_next_left().set_previous_left(previousLeft)
                currentNode.get_next_left().set_previous_right(currentNode)
                previousLeft.set_next_right(currentNode.get_next_left())
                
                if currentNode.get_value() == 1:
                    break
                
        
        currentNode.set_next_right(PascalNode(1))
        currentNode.get_next_right().set_previous_left(currentNode)
        
    def printTree(self):
        currentNode = self.rootNode
        for i in range(self.rowCount):
            self.printRow(currentNode)
            currentNode = currentNode.get_next_left()
            
    def printRow(self, baseNode):
        printString = ""
        currentNode = baseNode
        printString = printString + "1"
        if currentNode.get_previous_right() != None or currentNode.get_previous_left() != None:
            while True:
                currentNode = currentNode.get_previous_right()
                currentNode = currentNode.get_next_right()
                printString = printString + " " + str(currentNode.get_value())
                if currentNode.get_value() == 1:
                    break
        print(printString)
	
    def getNodeCount(self):
        currentRowCount = rowCount
        nodeCount = 0
        for __ in currentRowCount:
	        nodeCount = nodeCount + currentRowCount
	        currentRowCount = currentRowCount - 1
        return nodeCount
    def getRowCount(self):
        return self.rowCount
		
    def getRow(self, rowNum):
        currentNode = self.rootNode	
        while currentNode.get_next_left() != None:
            currentNode = currentNode.get_next_left()
		#node still exists here
        valueList = []
        if currentNode.get_next_left != None and currentNode.get_next_right != None and currentNode.get_previous_right != None:
            while True:
                currentNode = currentNode.get_previous_right()
                currentNode = currentNode.get_next_right()
                valueList.append(currentNode.get_value())
                if currentNode.get_value == 1:
                    break
        else:
            valueList.append(1)
        return valueList