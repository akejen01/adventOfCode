package se.adventsapp;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.lang3.StringUtils;

public class TriangleFileValidator {

	//Läser en fil, skapar trianglar och vet hur många som är valida och hur många som är invalida.

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

	public void readFileAndValidateTriangles() throws IOException{
		
		Triangle triangel = new Triangle();
		
		FileInputStream fstream = new FileInputStream(this.filename);
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

		String strLine;
		int rownum = 1;

		int a;
		int b;
		int c;
		
		while ((strLine = br.readLine()) != null)   {
		  String newString  = StringUtils.strip(strLine);
		  
		  List<String> numberList = Arrays.asList(newString.split("  "));
		  
		  
		  
		  
		  
		  a = Integer.parseInt(numberList.get(0).replaceAll(" ", ""));
		  b = Integer.parseInt(numberList.get(0).replaceAll(" ", ""));
		  c = Integer.parseInt(numberList.get(0).replaceAll(" ", ""));
		  
		  
		  
		  triangel.setSides(a,b,c);
		  System.out.println ("row: "+rownum +" : " + strLine + " är valid :" + triangel.isValid());
		  rownum++;
		}

		//Close the input stream
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
	
}

