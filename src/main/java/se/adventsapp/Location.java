package se.adventsapp;

public class Location {

	protected int x;
	protected int y;
	
	public Location(){
//		this.setX(0);
//		this.setY(0);
	}
	
	public Location(int x, int y) {
		this.setX(x);
		this.setY(y);
	}

	public Integer getX() {
		return this.x;
	}

	public Integer getY() {
		return this.y;
	}
	
	public void setX(Integer x){
		this.x = x;
	}
	
	public void setY(Integer y){
		this.y = y;
	}
}
