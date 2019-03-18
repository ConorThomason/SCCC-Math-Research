
class PascalTreeIterator:
    rootNode = None
    currentNode = None
    currentRow = 0
    def __init__(self, tree):
        self.rootNode = tree.getRootNode()
        self.currentNode = tree.getRootNode()
        
    def orderedNextNode(self):
        continueCheck = True
        nextRowCheck = True
        if self.currentNode.get_value() == 1:
            if self.currentNode.get_next_right() == None:
                nextRowCheck = False
            if nextRowCheck != False:
                if self.hasRight() != True:
                    continueCheck = False
                    
        if continueCheck == False and nextRowCheck == True:
            while self.currentNode.get_previous_left != None:
                self.moveLeft()
            self.nextRowLeft()
        elif nextRowCheck == False:
            pass
        else:
            self.moveRight()
    
    def hasRight(self):
        if self.currentNode.get_previous_right() != None:
            if self.currentNode.get_previous_right().get_next_right() != None:
                return True
        return False
    def hasLeft(self):
        if self.currentNode.get_previous_left().get_next_left() != None:
            return True
        return False
    def moveLeft(self):
        #Will do nothing if it can't move any further along the row.
        if self.currentNode.get_previous_left() != None and self.currentNode.get_next_left() != None:
            self.currentNode = self.currentNode.get_previous_left()
            self.currentNode = self.currentNode.get_next_left()
            
    def moveRight(self):
        if self.currentNode.get_previous_right() != None and self.currentNode.get_next_right() != None:
            self.currentNode = self.currentNode.get_previous_right()
            self.currentNode = self.currentNode.get_next_left()
    
    def hasNextRowLeft(self):
        if self.currentNode.get_next_left() != None:
            return True
        
        return False
    def hasNextRowRight(self):
        if self.currentNode.get_next_right() != None:
            return True
        
        return False
    def nextRowLeft(self):
        if self.hasNextRowLeft():
            self.currentNode = self.currentNode.get_next_left()
    
    def nextRowRight(self):
        if self.hasNextRowRight():
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
    def goToRoot(self):
        self.currentNode = self.rootNode