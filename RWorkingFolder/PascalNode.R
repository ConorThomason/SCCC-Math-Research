#Declarations and methods for Pascal Node
setClass("PascalNode", slots=list(value = "numeric", previousLeft="NULL", previousRight = "NULL", nextLeft = "NULL", nextRight = "NULL"))

#Don't need getters or setters, R can just reference them directly. Bit spooky considering I'm used to Java/Python/C++, but hey.