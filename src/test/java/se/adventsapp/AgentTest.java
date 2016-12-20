package se.adventsapp;


import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.CoreMatchers.*;

import org.junit.Test;



public class AgentTest {


	@Test
	public void enNyAgentStartarPåKändPositionRiktadÅtNorr() {
		Agent agenten = new Agent();
		assertThat(agenten.getHeading(), is("N"));
		assertThat(agenten.getLocation().getX(), is(0));
		assertThat(agenten.getLocation().getY(), is(0));
	}
	
	@Test
	public void enAgentVänderSigÅtRättHållBeroendePåVilketHållDenÄrRiktad(){
		Agent agenten = new Agent();
		assertThat(agenten.getHeading(), is("N"));
		agenten.turnLeft();
		assertThat(agenten.getHeading(), is("W"));
		agenten.turnLeft();
		assertThat(agenten.getHeading(), is("S"));
		agenten.turnRight();
		assertThat(agenten.getHeading(), is("W"));
	}
	
	@Test
	public void enAgentFårÄndradPositionNärDenRörSig(){
		Agent agenten = new Agent();
		agenten.moveAgent(2);
		assertThat(agenten.getLocation().getX(), is(0));
		assertThat(agenten.getLocation().getY(), is(2));
	}

	@Test
	public void enAgentRörSigEnligtEttKommando(){
		Agent agenten = new Agent();
		agenten.moveCommand("L3");
		assertThat(agenten.getHeading(), is("W"));
		assertThat(agenten.getLocation().getX(), is(-3));
		assertThat(agenten.getLocation().getY(), is(0));
	}
	
	@Test
	public void enAgentVetHurLångtDetÄrTillStarten(){
		Agent Agenten = new Agent(); 
		Agenten.moveCommand("R2");
		Agenten.moveCommand("L3");
		assertThat(Agenten.shortestPath(), is(5));

		Agenten.resetAgent();
		assertThat(Agenten.shortestPath(), is(0));
	}
	
	
	@Test
	public void enAgentRörSigEnligtEnSträngAvFleraKommandon(){

		Agent agenten = new Agent();

		agenten.moveCommandList("R2, L3");
		assertThat(agenten.shortestPath(), is(5));
		agenten.resetAgent();
		
		agenten.moveCommandList("R2, R2, R2");
		assertThat(agenten.shortestPath(), is(2));
		agenten.resetAgent();
		
		agenten.moveCommandList("R5, L5, R5, R3"); 
		assertThat(agenten.shortestPath(), is(12));
	}
	
	@Test
	public void enAgentLäggerEttSpårEfterSig(){
		
		Agent agenten = new Agent(); 
		agenten.moveCommand("R2");
		//assertThat(agenten.getLocationList().size(), is(3));
		assertThat(agenten.shortestPath(), is(2));
	}
	
	@Test
	public void enAgentHållerRedaPåNärDenPasserarEnPunktDenVaritPåFörut(){
		
		Agent agenten = new Agent();
		agenten.moveCommandList("R8, R4, R4, R8");
		assertThat(agenten.shortestPath(), is(8));
		//assertThat(agenten.firstIntersection(), is(4));
		System.out.println("Första korsningen:" + agenten.firstIntersection());
		System.out.println("Vägen fram: " + agenten.shortestPath());
		
	}
	
	@Test
	public void förstaProblemet(){
	
		Agent agenten = new Agent();
		
		agenten.moveCommandList("R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3");
		System.out.println("Vägen fram: " + agenten.shortestPath());
		
		
	}
	
	@Test
	public void andraProblemet(){
		Agent agenten = new Agent();
		
	}
	
}
