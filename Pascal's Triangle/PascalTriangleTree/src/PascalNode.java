import java.math.BigInteger;

public class PascalNode {
	
	private PascalNode previousLeftNode;
	private PascalNode previousRightNode;
	private PascalNode nextLeftNode;
	private PascalNode nextRightNode;
	private BigInteger value;
	
	public PascalNode(BigInteger value) {
		this.value = value;
	}
	public void setPreviousLeft(PascalNode previous) {
		this.previousLeftNode = previous;
	}
	public void setPreviousRight(PascalNode previous) {
		this.previousRightNode = previous;
	}
	public void setNextLeft(PascalNode next) {
		this.nextLeftNode = next;
	}
	public void setNextRight(PascalNode next) {
		this.nextRightNode = next;
	}
	public PascalNode getPreviousLeft() {
		return previousLeftNode;
	}
	public PascalNode getPreviousRight() {
		return previousRightNode;
	}
	public PascalNode getNextLeft() {
		return nextLeftNode;
	}
	public PascalNode getNextRight() {
		return nextRightNode;
	}
	public void setValue(BigInteger value) {
		this.value = value;
	}
	public BigInteger getValue() {
		return this.value;
	}
}
