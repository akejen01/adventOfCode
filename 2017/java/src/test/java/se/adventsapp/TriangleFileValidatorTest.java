package se.adventsapp;


import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.*;

import java.io.IOException;

import org.junit.Test;



public class TriangleFileValidatorTest {

	@Test
	public void kanLäsaEnFilRadvis() throws IOException {

		TriangleFileValidator tfv = new TriangleFileValidator("trianglar.txt");

		tfv.readFileRowAndValidateTriangles();
		System.out.println("invalida " + tfv.getNumOfInvalidTriangles());
		System.out.println("Valida " + tfv.getNumOfValidTriangles());
		
	}


	@Test
	public void kanLäsaEnFil3RaderItaget() throws Exception{
		
		TriangleFileValidator tfv = new TriangleFileValidator("trianglar.txt");
		
		tfv.readFile3RowAndValidateTriangels();
		
		System.out.println("invalida " + tfv.getNumOfInvalidTriangles());
		System.out.println("Valida " + tfv.getNumOfValidTriangles());
		
	}

}
