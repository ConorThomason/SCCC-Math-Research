source("PascalNode.R")
source("PascalTreeIterator.R")
setClass("PascalTree", slots=list(rootNode = "PascalNode", rowCount="numeric", nodeCount = "numeric"))

setMethod("show", "PascalTree", function(object){
  cat(object@rowCount, "\n")
  cat(object@nodeCount, "\n")
}
)


