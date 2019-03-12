package pascalsTriangle;
import javafx.application.Application;
import javafx.stage.Stage;

public class Start extends Application {

	@Override
	public void start(Stage primaryStage) throws Exception {
		TreeBuilder builder = new TreeBuilder(3);
		
//		VisGraph graph = new VisGraph();
//		VisNode node1 = new VisNode(1, "a");
//		VisNode node2 = new VisNode(2, "b");
//		VisEdge edge = new VisEdge(node1, node2, "", "");
//		graph.addNodes(node1, node2);
//		graph.addEdges(edge);
//		VisFx.graphNetwork(graph, primaryStage);
	}
	
	public static void main(String[] args) {
		launch(args);
//		PascalTree tree = new PascalTree(150);
//		tree.printTree();
//		System.out.println("Complete");
	}

}
 