package se.adventsapp;

import java.lang.Math;
import java.util.List;

import com.google.common.collect.Lists;


public class Agent {
	

	private Location location = new Location();
	private String riktning;

	private List<Location> locationList = Lists.newArrayList();
	
	public Agent() {
		this.riktning = "N";
		this.location.setX(0);
		this.location.setY(0);
	}

	public String getHeading() {
		return this.riktning;
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

	public void moveAgent(int steps) {
		
		switch (this.getHeading()) {
		case "N":
			this.location.y =this.location.y + steps;
			break;
		case "E":
			this.location.x = this.location.x + steps;
			break;
		case "S":
			this.location.y = this.location.y - steps;
			break;
		case "W":
			this.location.x = this.location.x - steps;
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
		this.moveAgent(Integer.parseInt(steps));
		
		// Här ska vi kolla om det är samma ställe som förut.
		
		
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
		
		return Math.abs(this.location.getX()) + Math.abs(this.location.getY());
	}

	public void resetAgent() {
		this.riktning = "N";
		this.location.x = 0;
		this.location.y = 0;
	}

	public Location getLocation() {
		
		return this.location;
	}

	public String firstIntersection() {
		// TODO Auto-generated method stub
		return null;
	}

	public List<Location> getLocationList() {
		// TODO Auto-generated method stub
		return this.locationList;
	}

}
