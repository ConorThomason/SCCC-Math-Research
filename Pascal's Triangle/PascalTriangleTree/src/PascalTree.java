import java.math.BigInteger;

public class PascalTree {

	private PascalNode rootNode;
	private int rowCount = 1;
	public PascalTree(int initialSize) {
		this.rootNode = new PascalNode(new BigInteger("1"));
		for (int i = 0; i < initialSize; i++) {
			generateNewRow();
			rowCount++;
		}
	}

	public void generateNewRow() {
		PascalNode currentNode = rootNode;
		boolean secondRow = false;
		PascalNode previousLeft;
		if (currentNode.getNextLeft() == null) {
			secondRow = true;
		}
		while (currentNode.getNextLeft() != null) {
			currentNode = currentNode.getNextLeft();
		}
		currentNode.setNextLeft(new PascalNode(new BigInteger("1")));
		currentNode.getNextLeft().setPreviousRight(currentNode);
		if (!secondRow) {
			do {

				previousLeft = currentNode;
				currentNode = currentNode.getPreviousRight();
				currentNode = currentNode.getNextRight();
				currentNode.setNextLeft(new PascalNode(previousLeft.getValue().add(currentNode.getValue())));

				currentNode.getNextLeft().setPreviousLeft(previousLeft);
				currentNode.getNextLeft().setPreviousRight(currentNode);
				previousLeft.setNextRight(currentNode.getNextLeft());
				
			} while (!currentNode.getValue().toString().equals("1"));
		}
		currentNode.setNextRight(new PascalNode(new BigInteger("1")));
		currentNode.getNextRight().setPreviousLeft(currentNode);
	}

	public void printTree() {
		PascalNode currentNode = rootNode;
		for (int i = 0; i < rowCount; i++) {
			printRow(currentNode);
			currentNode = currentNode.getNextLeft();
		}
	}

	public void printRow(PascalNode baseNode) {
		String printString = "";
		PascalNode currentNode = baseNode;
		printString += "1";
		if (!(currentNode.getPreviousRight() == null && currentNode.getPreviousLeft() == null)) {
			do {
				currentNode = currentNode.getPreviousRight();
				currentNode = currentNode.getNextRight();
				printString += " " + currentNode.getValue().toString();
			} while (!currentNode.getValue().toString().equals("1"));
		}
		System.out.println(printString);
	}

}
