package Frames;

// Represents a single card
public class Card {
	
	private String name;
	private Game game;

	public Card(String name, Game game) {
		this.name = name;
		this.game = game;
	}
	
	public String getName() {
		return this.name;
	}
	
	public Game getGame() {
		return this.game;
	}
	
}