class PascalTreeIterator:
    currentNode = None
    currentRow = 0
    def __init__(self, tree):
        self.currentNode = tree.getRootNode()
        
    def orderedNextNode(self):
        continueCheck = True
        nextRowCheck = True
        if self.currentNode.get_value() == 1:
            if self.currentNode.get_next_right() == None:
                nextRowCheck = False
        
        if continueCheck == False and nextRowCheck == True:
            while self.currentNode.get_previous_left != None:
                self.moveLeft(self)
            self.nextRowLeft(self)
        elif nextRowCheck == False:
            pass
        else:
            self.moveRight()
    
    def moveLeft(self):
        #Will do nothing if it can't move any further along the row.
        if self.currentNode.get_previous_left() != None and self.currentNode.get_next_left() != None:
            self.currentNode = self.currentNode.get_previous_left()
            self.currentNode = self.currentNode.get_next_left()
            
    def moveRight(self):
        if self.currentNode.get_previous_right() != None and self.currentNode.get_next_right() != None:
            self.currentNode = self.currentNode.get_previous_right()
            self.currentNode = self.currentNode.get_next_left()
            
    def nextRowLeft(self):
        self.currentNode = self.currentNode.get_next_left()
    
    def nextRowRight(self):
        self.currentNode = self.currentNode.get_next_right()
        
    def getCurrentNode(self):
        return self.currentNode
    
    def hasOrderedNext(self):
        previousNode = self.currentNode
        self.orderedNextNode()
        if previousNode == self.currentNode:
            return False
        else:
            return True