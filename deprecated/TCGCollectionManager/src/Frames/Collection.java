package Frames;

import java.io.Serializable;
import java.util.ArrayList;

public class Collection implements Serializable {
	
	private static final long serialVersionUID = -1006038138527537901L;
	private String name;
	private Game game;
	public ArrayList<Card> cards;
	
	public Collection(String name, Game game) {
		this.name = name;
		this.game = game;
		this.cards = new ArrayList<Card>();
	}
	
	public String getName() {
		return this.name;
	}
	
	public Game getGame() {
		return this.game;
	}
	
	public void addCard(Card card) {
		this.cards.add(card);
	}
}