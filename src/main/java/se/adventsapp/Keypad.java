package se.adventsapp;

import java.util.List;

public abstract class Keypad {

	protected char currentKey;
	

	public char getCurrentKey() {

		return this.currentKey;
	}


	abstract public void moveCommand(String string); 

	public void moveCommandList(List<String> commandList){
		
		for (String commandString : commandList) {
			this.moveCommand(commandString);
		}
		
	}
	
	public void moveCommandList(String string) {
		
		String[] listan = string.split("");
		
		System.out.println("Längd :" + listan.length);
		
		for (String commandString : listan) {
			this.moveCommand(commandString);
		}
		
	}
	
}
