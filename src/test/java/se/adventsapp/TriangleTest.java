package se.adventsapp;


import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.*;

import org.junit.Test;



public class TriangleTest {

	@Test
	public void enTriangelSomÄrNyÄrValid() {
		
		Triangle triangel = new Triangle();
		assertThat(triangel.isValid(), is(true));
	}

	@Test
	public void detGårAttSättaSidornaPåEnTriangelMedEttAnropOchHämtaDem(){
		Triangle triangel = new Triangle();
		triangel.setSides(5,6,4);
		assertThat(triangel.getSides(), is("5,6,4"));
	}
	
	@Test
	public void enInkorrektTriangelÄrInteValid(){
		Triangle triangel = new Triangle();

		// Dvs ingen av sidorna är större än de andra två tillsammans.
		triangel.setSides(5,6,4);
		assertThat(triangel.isValid(), is(true));

		// Dvs en av sidorna är större än de andra två tillsammans.
		triangel.setSides(5,10,25);
		assertThat(triangel.isValid(), is(false));
		
		triangel.setSides(25,5,10);
		assertThat(triangel.isValid(), is(false));
		
		triangel.setSides(10,25,5);
		assertThat(triangel.isValid(), is(false));
		
	}

}
