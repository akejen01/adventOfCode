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
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + x;
		result = prime * result + y;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Location other = (Location) obj;
		if (x != other.x)
			return false;
		if (y != other.y)
			return false;
		return true;
	}
	
}
