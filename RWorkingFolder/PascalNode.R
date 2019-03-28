#Declarations and methods for Pascal Node

setClass("PascalNode", slots=list(value = "numeric", previousLeft="MaybeNode", previousRight = "MaybeNode", nextLeft = "MaybeNode", nextRight = "MaybeNode"), prototype=prototype(previousLeft = NULL, previousRight = NULL, nextLeft = NULL, nextRight = NULL))

setClassUnion("MaybeNode", c("PascalNode", "NULL"))
#Don't need getters or setters, R can just reference them directly. Bit spooky considering I'm used to Java/Python/C++, but hey.