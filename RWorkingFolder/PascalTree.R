source("PascalNode.R")
source("PascalTreeIterator.R")
setClass("PascalTree", slots=list(rootNode = "PascalNode", rowCount="numeric", nodeCount = "numeric"))

setMethod("show", "PascalTree", function(object){
  cat(object@rowCount, "\n")
  cat(object@nodeCount, "\n")
}
)

setGeneric("constructTree", function(object, providedRowCount) standardGeneric("constructTree"))
setMethod("constructTree", "PascalTree", function(object, providedRowCount) {
  eval.parent(substitute(object@rootNode <- new("PascalNode", value = 1))) #Constructs the root node
  currentRowCount <- object@rowCount
  for (i in seq(providedRowCount)){
    generateNewRow(object)
    currentRowCount = currentRowCount + 1
  }
  eval.parent(substitute(object@rowCount <- currentRowCount))
  generateNodeCount(object)
}
)

setGeneric("generateNewRow", function(object) standardGeneric("generateNewRow"))
setMethod("generateNewRow", "PascalTree", function(object){
   iterator <- new("PascalTreeIterator")
   constructIterator(iterator, object)
   currentNode <- object@rootNode
   secondRow = FALSE
   
   if (hasLeft(iterator)){
     secondRow = TRUE
   }
   
   while(hasNextRowLeft(iterator)){
     nextRowLeft(iterator)
   }
   newNode = new("PascalNode", value = 1)
   eval.parent(substitute(object@currentNode@nextLeft <- newNode))
   eval.parent(substitute(object@currentNode@nextLeft@previousRight <- object@currentNode))
   
   if (secondRow == FALSE){
     repeat{
       previousLeft <- object@currentNode
       orderedNextNode(iterator)
       currentNode = getCurrentNode(iterator)
       currentNode@nextLeft <- new("PascalNode", value = (previousLeft@value + currentNode@value))
       
       currentNode@nextLeft@previousLeft <- previousLeft
       currentNode@nextLeft@previousRight <- currentNode
       previousLeft@nextRight <- currentNode@nextLeft
       if (currentNode@value == 1){
         break
       }
     }
     browser()
   }
}
)

setGeneric("printTree", function(object) standardGeneric("printTree"))
setMethod("printTree", "PascalTree", function(object){
  currentNode = object@rootNode
  for (i in seq(object@rowCount))
  {
    printRow(currentNode)
    currentNode <- currentNode@nextLeft
  }
}
)

setGeneric("printRow", function(object, baseNode) standardGeneric("printRow"))
setMethod("printRow", "PascalTree", function(object, baseNode){
  printString = ""
  currentNode = baseNode
  paste(printString, "1")
  if (!is.null(currentNode@previousRight) || !is.null(currentNode@previousLeft)){
    repeat{
      currentNode <- currentNode@previousRight
      currentNode <- currentNode@nextRight
      paste(printString, currentNode@value, sep = " ")
      if (currentNode@value == 1){
        break
      }
    }
  }
  cat(printString)
}
)

setGeneric("generateNodeCount", function(object) standardGeneric("generateNodeCount"))
setMethod("generateNodeCount", "PascalTree", function(object){
    n <- object@rowCount
    n = (n*(n+1))/2
    eval.parent(substitute(object@nodeCount <- n))
}
)

