package pascalsTriangle;

import graph.VisEdge;
import graph.VisGraph;
import graph.VisNode;

public class TreeBuilder {
	private PascalTree tree;
	private VisGraph graph;
	private PascalNode currentNode;

	public TreeBuilder(int initialSize) {
		this.tree = new PascalTree(initialSize);
		graph = new VisGraph();
		buildGraph();
	}
	public void buildGraph() {
		currentNode = tree.getRootNode();
		PascalNode initialNode = currentNode;
		int nodeId = 1;
		VisNode node = new VisNode(1, currentNode.getValue().toString());
		VisNode leftNode;
		VisNode rightNode;
		VisEdge leftEdge;
		VisEdge rightEdge;
		graph.addNodes(node);
		do {
			do  {
				leftNode = new VisNode(nodeId++, currentNode.getNextLeft().getValue().toString());
				rightNode = new VisNode(nodeId++, currentNode.getNextRight().getValue().toString());
				leftEdge = new VisEdge(node, leftNode, "", "");
				rightEdge = new VisEdge(node, rightNode, "", "");
				graph.addNodes(leftNode, rightNode);
				graph.addEdges(leftEdge, rightEdge);
				if (currentNode.hasPreviousRight()) {
					currentNode = currentNode.getPreviousRight();
					currentNode = currentNode.getNextRight();
				}
			} while (currentNode.hasPreviousRight());
			initialNode = initialNode.getNextLeft();
		} while (initialNode.hasNextLeft());
	}
	public VisGraph getGraph() {
		return graph;
	}
}
