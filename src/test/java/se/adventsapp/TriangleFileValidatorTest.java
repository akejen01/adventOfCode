package se.adventsapp;


import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.*;

import java.io.IOException;

import org.junit.Test;



public class TriangleFileValidatorTest {

	@Test
	public void kanLäsaEnFil() throws IOException {

		TriangleFileValidator tfv = new TriangleFileValidator("trianglar.txt");

		tfv.readFileAndValidateTriangles();
		System.out.println("invalida " + tfv.getNumOfInvalidTriangles());
		System.out.println("Valida " + tfv.getNumOfValidTriangles());
		
	}



}
