library(reticulate)
source_python("Start.py")
begin(100)
nodes <- read.csv("nodes.csv", header=T, as.is=T)
links <- read.csv("edges.csv", header=T, as.is=T)

head(nodes)
head(links)

nodes$x <- nodes$x*20
nodes$y <- nodes$y*20

library("igraph")
net <- graph_from_data_frame(d=links, vertices=nodes, directed=T)
net <- simplify(net, remove.multiple = F, remove.loops = T)
#plot(net, edge.arrow.size=.4, vertex.label=V(net)$value)
library("visNetwork")
#visNetwork(nodes, links, width="100%", height="100%", main="Pascal's Triangle")

vis.nodes <- nodes
vis.links <- links

vis.nodes$shape <- "dot"
vis.nodes$shadow <- TRUE
vis.nodes$title <- vis.nodes$value
vis.nodes$label <- vis.nodes$value

vis.nodes$color.background <- "gold"
vis.nodes$color.border <- "black"
vis.nodes$color.highlight.background <- "orange"
vis.nodes$color.highlight.border <- "darkred"
network <- visNetwork(vis.nodes, vis.links, width = "1920px", height = "1080px", main="Pascal's Triangle") %>%
  visNodes(fixed = TRUE)
network %>% visSave(file = "graph.html", background = "white")