package se.adventsapp;

public class Triangle {

	int sideA;
	int sideB;
	int sideC;

	public Triangle() {
		this.setSides(5, 5, 5);
	}

	public boolean isValid() {

		//System.out.println("Trangel: "+ this.toString());
		
		if ((this.sideA + this.sideB) > this.sideC && (this.sideB + this.sideC) > this.sideA && (this.sideA + this.sideC) > this.sideB ){
			return true;
		} else {
			return false;
		}

	}

	public void setSides(int a, int b, int c) {
		this.sideA = a;
		this.sideB = b;
		this.sideC = c;
	}

	public String getSides() {

		return this.toString();
	}
	
	

	@Override
	public String toString() {
		return this.sideA + "," + this.sideB + "," + this.sideC;
	}

}
