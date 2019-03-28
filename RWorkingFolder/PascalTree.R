source("PascalNode.R")
source("PascalTreeIterator.R")
setClass("PascalTree", slots=list(rootNode = "PascalNode", rowCount="numeric", nodeCount = "numeric"))

setMethod("show", "PascalTree", function(object){
  cat(object@rowCount, "\n")
  cat(object@nodeCount, "\n")
}
)

setGeneric("constructTree", function(object, value) standardGeneric("constructTree"))
setMethod("constructTree", "PascalTree", function(object, value){
  eval.parent(substitute(object@rootNode <- new("PascalNode", value = 1)))
  eval.parent(substitute(object@rowCount <- value))
  for (i in seq(value)){
    generateNewRow(object)
  }
  browser()
}
)

setGeneric("generateNewRow", function(object) standardGeneric("generateNewRow"))
setMethod("generateNewRow", "PascalTree", function(object){
    currentNode = object@rootNode
    secondRow = FALSE
    if (is.null(currentNode@nextLeft)){
      secondRow = TRUE
    }
    
    while (!is.null(currentNode@nextLeft)){
      currentNode <- currentNode@nextLeft
    }
    
    currentNode@nextLeft <- new("PascalNode", value = 1)
    currentNode@nextLeft@previousRight <- currentNode
    
    if (!secondRow){
      repeat{
        previousLeft <- currentNode
        currentNode <- currentNode@previousRight
        currentNode <- currentNode@nextRight
        currentNode@nextLeft <- new("PascalNode", value = (previousLeft@value + currentNode@value))
        
        currentNode@nextLeft@previousRight <- previousLeft
        currentNode@nextLeft@previousRight <- currentNode
        previousLeft@nextRight <- currentNode@nextLeft
        
        if (currentNode@value == 1){
          break
        }
      }
    }
    
    currentNode@nextRight <- new("PascalNode", value = 1)
    currentNode@nextRight@previousLeft <- currentNode
}
)

setGeneric("printTree", function(object) standardGeneric("printTree"))
setMethod("printTree", "PascalTree", function(object){
  currentNode <- object@rootNode
  for (i in seq(object@rowCount)){
    printRow(object, currentNode)
    currentNode <- currentNode@nextLeft
  }
}
)

setGeneric("printRow", function(object, baseNode) standardGeneric("printRow"))
setMethod("printRow", "PascalTree", function(object, baseNode){
  printString <- ""
  currentNode <- baseNode
  paste(printString, "1")
  if (!is.null(currentNode@previousRight) | !is.null(currentNode@previousLeft)){
    repeat{
      currentNode <- currentNode@previousRight
      currentNode <- currentNode@nextRight
      paste(printString, currentNode@value, sep=" ")
      if (currentNode@value == 1){
        break
      }
    }
  }
  browser()
  print(printString)
}
)