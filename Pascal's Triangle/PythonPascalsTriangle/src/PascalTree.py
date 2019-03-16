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
        for __ in range(self.rowCount):
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
	
    def getRootNode(self):
        return self.rootNode
    
    def getNodeCount(self):
        n = self.rowCount - 1
        n = (n*(n+1))//2
        return n
    def getRowCount(self):
        return self.rowCount
		
    def getRow(self, rowNum):
        currentNode = self.rootNode	
        for __ in range(rowNum):
            currentNode = currentNode.get_next_left()
		#node still exists here
        valueList = []
        valueList.append(1)
        while True:
            if currentNode.get_value() != 1:
                currentNode = currentNode.get_previous_right()
                currentNode = currentNode.get_next_right()
                valueList.append(currentNode.get_value())
            else:
                valueList.append(1)
                break
        return valueList