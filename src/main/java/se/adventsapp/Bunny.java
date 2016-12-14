package se.adventsapp;

import java.lang.Math;


public class Bunny {
	
	private int x;
	private int y;
	private String riktning;

	public Bunny() {
		this.riktning = "N";
		this.x = 0;
		this.y = 0;
	}

	public String getHeading() {
		return this.riktning;
	}

	public Integer getX() {
		return this.x;
	}

	public Integer getY() {
		return this.y;
	}

	public void turnLeft() {

		switch (this.getHeading()) {
		case "N":
			this.riktning = "W";
			break;
		case "W":
			this.riktning = "S";
			break;
		case "S":
			this.riktning = "E";
			break;
		case "E":
			this.riktning = "N";
			break;
		}

	}

	public void turnRight() {
		
		switch (this.getHeading()) {
		case "N":
			this.riktning = "E";
			break;
		case "E":
			this.riktning = "S";
			break;
		case "S":
			this.riktning = "W";
			break;
		case "W":
			this.riktning = "N";
			break;
		}

	}

	public void moveBunny(int steps) {
		
		switch (this.getHeading()) {
		case "N":
			this.y = this.y + steps;
			break;
		case "E":
			this.x = this.x + steps;
			break;
		case "S":
			this.y = this.y - steps;
			break;
		case "W":
			this.x = this.x - steps;
			break;
		}
		
	}

	public void moveCommand(String string) {

		if (string.contains("L")){
			this.turnLeft();
		} else {
			this.turnRight();
		}
		
		String steps = string.substring(1);
		this.moveBunny(Integer.parseInt(steps));
		
	}

	public void moveCommandList(String string) {

		string = string.replaceAll("\\s+","");
		String[] theCommandList = string.split(",");
	
		for (String commandItem : theCommandList) {
//			System.out.println("Skriv ut: " +commandItem);
			this.moveCommand(commandItem);
		}
		
	}

	public Integer shortestPath() {
//		System.out.println("X:"+  this.x);
//		System.out.println("Y:"+  this.y);
		
		return Math.abs(x) + Math.abs(y);
	}

	public void resetBunny() {
		this.riktning = "N";
		this.x = 0;
		this.y = 0;
	}

}
