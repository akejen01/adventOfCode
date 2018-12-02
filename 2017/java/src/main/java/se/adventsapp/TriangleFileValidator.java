package se.adventsapp;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.lang3.StringUtils;

import com.google.common.collect.Lists;

public class TriangleFileValidator {

	// Läser en fil, skapar trianglar och vet hur många som är valida och hur
	// många som är invalida.

	String filename;

	int numOfValidTriangles;
	int numOfInvalidTriangles;

	public TriangleFileValidator() {
		this.filename = "";
		this.setNumOfInvalidTriangles(0);
		this.setNumOfValidTriangles(0);

	}

	public TriangleFileValidator(String filename) {
		this.filename = filename;
		this.setNumOfInvalidTriangles(0);
		this.setNumOfValidTriangles(0);

	}

	
	public void readFileRowAndValidateTriangles() throws IOException {

		Triangle triangel = new Triangle();

		FileInputStream fstream = new FileInputStream(this.filename);
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

		String strLine;
		int rownum = 1;

		int a;
		int b;
		int c;

		while ((strLine = br.readLine()) != null) {

			a = Integer.parseInt(strLine.substring(0, 5).trim());
			b = Integer.parseInt(strLine.substring(6, 10).trim());
			c = Integer.parseInt(strLine.substring(11).trim());

			triangel.setSides(a, b, c);

			if (triangel.isValid()) {
				this.numOfValidTriangles++;
			} else {
				this.numOfInvalidTriangles++;
			}
			rownum++;
		}
		br.close();
	}

	public int getNumOfValidTriangles() {
		return numOfValidTriangles;
	}

	public void setNumOfValidTriangles(int numOfValidTriangles) {
		this.numOfValidTriangles = numOfValidTriangles;
	}

	public int getNumOfInvalidTriangles() {
		return numOfInvalidTriangles;
	}

	public void setNumOfInvalidTriangles(int numOfInvalidTriangles) {
		this.numOfInvalidTriangles = numOfInvalidTriangles;
	}

	public void readFile3RowAndValidateTriangels() throws Exception {

		Triangle triangelColumn1 = new Triangle();
		Triangle triangelColumn2 = new Triangle();
		Triangle triangelColumn3 = new Triangle();

		FileInputStream fstream = new FileInputStream(this.filename);
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

		String strLine;


		List<Integer> column1 = Lists.newArrayList();
		List<Integer> column2 = Lists.newArrayList();
		List<Integer> column3 = Lists.newArrayList();

		/*
		 * Läs hela filen rad för rad. Lägg datat i 3 olika listor (int)
		 * 
		 * Loopa över listan i steg om 3 och skapa trianglar.
		 * 
		 */

		while ((strLine = br.readLine()) != null) {

			column1.add(Integer.parseInt(strLine.substring(0, 5).trim()));
			column2.add(Integer.parseInt(strLine.substring(6, 10).trim()));
			column3.add(Integer.parseInt(strLine.substring(11).trim()));

		}
		br.close();
		
		// Utgår ifrån att det finns lika många i varje lista...
		
		for (int i = 0; i < column1.size(); i += 3 ) {
			
			triangelColumn1.setSides(column1.get(i), column1.get(i+1), column1.get(i+2));
			triangelColumn2.setSides(column2.get(i), column2.get(i+1), column2.get(i+2));
			triangelColumn3.setSides(column3.get(i), column3.get(i+1), column3.get(i+2));
			
			validateTriangle(triangelColumn1);
			validateTriangle(triangelColumn2);
			validateTriangle(triangelColumn3);
			
		}
		
	}

	private void validateTriangle(Triangle triangle) {
		if (triangle.isValid()) {
//		System.out.println("Sidor: "+ triangle.getSides());	
			
			this.numOfValidTriangles++;
		} else {
			this.numOfInvalidTriangles++;
		}
	}

	public void resetCounters() {

		this.setNumOfInvalidTriangles(0);
		this.setNumOfValidTriangles(0);
		
	}

}
