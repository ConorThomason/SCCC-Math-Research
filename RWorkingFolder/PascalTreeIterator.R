#Declarations and methods for PascalTreeIterator
setClass("PascalTreeIterator", slots=list(rootNode = "PascalNode", currentNode = "PascalNode", currentRow = "numeric"))

setGeneric("constructIterator", function(object, tree) standardGeneric("constructIterator"))
setMethod("constructIterator", "PascalTreeIterator", function(object, tree){
  n <- tree@rootNode
  eval.parent(substitute(object@rootNode <- n))
  eval.parent(substitute(object@currentNode <- n))
}
)

setGeneric("orderedNextNode", function(object) standardGeneric("orderedNextNode"))
setMethod("orderedNextNode", "PascalTreeIterator", function(object){
  if (hasRight(object))
  {
    moveRight(object)
  }
  else{
    if (hasNextRowRight(object))
    {
      while (hasLeft(object)){
        moveLeft(object)
      }
      nextRowLeft(object)
    }
  }
}
)

setGeneric("isRootNode", function(object) standardGeneric("isRootNode"))
setMethod("isRootNode", "PascalTreeIterator", function(object){
  if(is.null(object@currentNode@previousLeft) && is.null(object@currentNode@previousRight)){
    return(TRUE)
  }
  return(FALSE)
}
)

setGeneric("nextRowLeft", function(object) standardGeneric("nextRowLeft"))
setMethod("nextRowLeft", "PascalTreeIterator", function(object){
  if (hasNextRowLeft(object)){
    eval.parent(substitute(object@currentNode <- object@currentNode@nextLeft))
  }
}
)

setGeneric("hasNextRowLeft", function(object) standardGeneric("hasNextRowLeft"))
setMethod("hasNextRowLeft", "PascalTreeIterator", function(object){
  if(is.null(object@currentNode@nextRight) == FALSE){
    return(TRUE)
  }
  return(FALSE)
}
)

setGeneric("moveLeft", function(object) standardGeneric("moveLeft"))
setMethod("moveLeft", "PascalTreeIterator", function(object){
  eval.parent(substitute(object@currentNode <- object@currentNode@previousLeft))
  eval.parent(substitute(object@currentNode <- object@currentNode@nextLeft))
}
)

setGeneric("hasLeft", function(object) standardGeneric("hasLeft"))
setMethod("hasLeft", "PascalTreeIterator", function(object){
  if(is.null(object@currentNode@previousLeft) == FALSE){
    if (is.null(object@currentNode@previousLeft@nextLeft) == FALSE){
      return(TRUE)
    }
  }
  return(FALSE)
}
)

setGeneric("hasRight", function(object) standardGeneric("hasRight"))
setMethod("hasRight", "PascalTreeIterator", function(object){
  if (is.null(object@currentNode@previousRight) == FALSE) {
    if (is.null(object@currentNode@previousRight@nextRight) == FALSE){
      return(TRUE)
    }
  }
  return(FALSE)
}
)

setGeneric("moveRight", function(object) standardGeneric("moveRight"))
setMethod("moveRight", "PascalTreeIterator", function(object){
  eval.parent(substitute(object@currentNode <- object@currentNode@previousRight))
  eval.parent(substitute(object@currentNode <- object@currentNode@nextRight))
}
)

setGeneric("hasNextRowRight", function(object) standardGeneric("hasNextRowRight"))
setMethod("hasNextRowRight", "PascalTreeIterator", function(object){
  if(is.null(object@currentNode@nextLeft)== FALSE){
    return(TRUE)
  }
}
)
setGeneric("goToRoot", function(object) standardGeneric("goToRoot"))
setMethod("goToRoot", "PascalTreeIterator", function(object){
  eval.parent(substitute(object@currentNode <- object@rootNode))  
}
)

setGeneric("getCurrentNode", function(object) standardGeneric("getCurrentNode"))
setMethod("getCurrentNode", "PascalTreeIterator", function(object){
  return(object@currentNode)  
}
)
