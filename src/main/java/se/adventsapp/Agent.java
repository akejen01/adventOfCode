package se.adventsapp;

import java.lang.Math;
import java.util.HashMap;
import java.util.List;

import com.google.common.collect.Lists;


public class Agent {
	

	private Location location = new Location();
	private String riktning;
	private boolean intersection = false;
	
	
	List<String> locationList =  Lists.newArrayList();

	
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
			for (int i = 0; i < steps; i++) {
				checkForIntersection(this.location.x+":"+(this.location.y + i));
				this.locationList.add(this.location.x+":"+(this.location.y + i));
			}
			this.location.y =this.location.y + steps;
			break;
		case "E":
			for (int i = 0; i < steps; i++) {
				checkForIntersection((this.location.x + i) +":"+ this.location.y);
				this.locationList.add((this.location.x + i) +":"+ this.location.y);
			}
			this.location.x = this.location.x + steps;
			break;
		case "S":
			for (int i = 0; i < steps; i++) {
				checkForIntersection(this.location.x +":"+ (this.location.y - i));
				this.locationList.add(this.location.x +":"+ (this.location.y - i));
			}
			this.location.y = this.location.y - steps;
			break;
		case "W":
			for (int i = 0; i < steps; i++) {
				checkForIntersection((this.location.x - i) +":"+ this.location.y);
				this.locationList.add((this.location.x - i) +":"+ this.location.y);
			}
			this.location.x = this.location.x - steps;
			break;
		}
		
	}

	private void checkForIntersection(String string) {
		if (!this.intersection){
		// Utvärdera bara om vi inte har hittat första korsningen.
		if (this.locationList.contains(string)){
			//Korsning! 
			System.out.println("Korsning vid : " + string);
			this.intersection = true;
		 }
		
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
		
	}

	public void moveCommandList(String string) {

		string = string.replaceAll("\\s+","");
		String[] theCommandList = string.split(",");
		for (String commandItem : theCommandList) {
			this.moveCommand(commandItem);
		}
		
	}

	public Integer shortestPath() {
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

	public String firstIntersectionShortestPath() {
		// TODO Auto-generated method stub
		return null;
	}

	public List<String> getLocationList() {
		return this.locationList;
	}

}
