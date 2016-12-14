package se.adventsapp;


import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.*;

import org.junit.Test;



public class BunnyTest {


	@Test
	public void enNyKaninStartarPåKändPositionRiktadÅtNorr() {
		Bunny kaninen = new Bunny();
		assertThat(kaninen.getHeading(), is("N"));
		assertThat(kaninen.getX(), is(0));
		assertThat(kaninen.getY(), is(0));
	}

	@Test
	public void enKaninVänderSigÅtRättHållBeroendePåVilketHållDenÄrRiktad(){
		Bunny kaninen = new Bunny();
		assertThat(kaninen.getHeading(), is("N"));
		kaninen.turnLeft();
		assertThat(kaninen.getHeading(), is("W"));
		kaninen.turnLeft();
		assertThat(kaninen.getHeading(), is("S"));
		kaninen.turnRight();
		assertThat(kaninen.getHeading(), is("W"));
	}
	
	@Test
	public void enKaninFårÄndradPositionNärDenRörSig(){
		Bunny kaninen = new Bunny();
		kaninen.moveBunny(2);
		assertThat(kaninen.getX(), is(0));
		assertThat(kaninen.getY(), is(2));
	}

	@Test
	public void enKaninRörSigEnligtEttKommando(){
		Bunny kaninen = new Bunny();
		kaninen.moveCommand("L3");
		assertThat(kaninen.getHeading(), is("W"));
		assertThat(kaninen.getX(), is(-3));
		assertThat(kaninen.getY(), is(0));
	}
	
	@Test
	public void enKaninVetHurLångtDetÄrTillStarten(){
		Bunny kaninen = new Bunny(); 
		kaninen.moveCommand("R2");
		kaninen.moveCommand("L3");
		assertThat(kaninen.shortestPath(), is(5));

		kaninen.resetBunny();
		assertThat(kaninen.shortestPath(), is(0));
	}
	
	
	@Test
	public void enKaninRörSigEnligtEnSträngAvFleraKommandon(){

		Bunny kaninen = new Bunny();

		kaninen.moveCommandList("R2, L3");
		assertThat(kaninen.shortestPath(), is(5));
		kaninen.resetBunny();
		
		kaninen.moveCommandList("R2, R2, R2");
		assertThat(kaninen.shortestPath(), is(2));
		kaninen.resetBunny();
		
		kaninen.moveCommandList("R5, L5, R5, R3"); 
		assertThat(kaninen.shortestPath(), is(12));
	}
	
	@Test
	public void bunnyProblem(){
	
		Bunny kaninen = new Bunny();
		
		kaninen.moveCommandList("R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3");
		System.out.println("Vägen fram: " + kaninen.shortestPath());
		
	}
	
	
}
