setClass("PascalNode", slots=list(value = "numeric", previousLeft="PascalNode", previousRight = "PascalNode", nextLeft = "PascalNode", nextRight = "PascalNode"))
setClass("PascalTree", slots=list(rootNode = "PascalNode", rowCount="numeric"))
setClass("PascalTreeIterator", slots=list(rootNode = "PascalNode", currentNode = "PascalNode", currentRow = "numeric"))

setMethod("show", "PascalNode", function(object){
  cat("Value = ", object@value, "\n")
}
)
