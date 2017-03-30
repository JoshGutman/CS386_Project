package Frames;

import java.io.Serializable;

// Represents a single card
public class Card implements Serializable {
	
	private static final long serialVersionUID = 6983955067741736930L;
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