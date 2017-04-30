package Frames;

import java.io.Serializable;

// Represents a TCG
public class Game implements Serializable {
	
	private static final long serialVersionUID = 5484444498579123804L;
	private String name;
	
	public Game(String name) {
		this.name = name;
	}
	
	public String getName() {
		return this.name;
	}
}