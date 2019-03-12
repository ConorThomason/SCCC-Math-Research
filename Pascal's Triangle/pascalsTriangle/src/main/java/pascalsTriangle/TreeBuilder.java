package pascalsTriangle;

import com.fxgraph.cells.RectangleCell;
import com.fxgraph.graph.Graph;
import com.fxgraph.graph.ICell;
import com.fxgraph.graph.Model;
import com.fxgraph.*;

public class TreeBuilder {
	private PascalTree tree;
	private Graph graph = new Graph();
	private Model model = graph.getModel();
	private PascalNode currentNode;

	public TreeBuilder(int initialSize) {
		this.tree = new PascalTree(initialSize);
		buildGraph();
	}
	public void buildGraph() {
		graph.beginUpdate();
		final ICell cell = new RectangleCell();
		model.addCell(cell);
		graph.endUpdate();
	}
	public Graph getGraph() {
		return graph;
	}
}
