import java.util.ArrayList;
import java.util.List;
import java.util.Random;

//So this is my native class
public class MyTest_scheduler {
	
	//Random number generator object
	static Random randomGenerator=new Random();
	//make static variables for traps and decisions
	static List <Integer> traps=new ArrayList<Integer>();
	static List <Boolean> decisions=new ArrayList<Boolean>();
	static int decision_counter=0;
	static int trap_counter=0;
	
	//lets make two inner classes which can do two processes
	//This class do the analysis: Should be a daemon process
	//This class receives the incoming message
	
	//This class receives the incoming message
	public static  class Analyzer extends Thread {
		int iteration=0;
		public void run(){
			try {
				iteration++;
				System.out.println("Entering Analyzer Thread "+iteration+" th time");
				System.out.println("Making Analysis");
				if (randomGenerator.nextBoolean()){
					decisions.add(true);
				} else{
					decisions.add(false);
				}
				System.out.println("Exiting the anlayzer");
				//increment the decision counter 
				decision_counter+=1;
				//calling propogator
				System.out.println("Starting the propogator");
				Propogator p = new Propogator();
				p.start();
				System.out.println("Exiting the anlayzer");
			} catch (Exception e) {
				System.out.println("wao bc ");
			}
		}
		//end of class:Analyzer
	}
	
	//This class receives the incoming message
	public static class Trap extends Thread {
		
		public void run(){
			
		}
		//end of class:Trap
	}
	
	//This function propagates the decision when made by analyzer
	//should be a daemon process
	public static class Propogator extends Thread {
		
		public void run (){
			System.out.println("Entering Propogator Thread");
			System.out.println("The decision for "+traps.get(trap_counter-1)+" is "+decisions.get(decision_counter-1));
			System.out.println("Exiting Propogator Thread");
		}
		//end of class:Proporgator
	}
	
	protected int generator (){
		return randomGenerator.nextInt();
		//end of generator
	}
	
	//main function 
	public static void main (String[] args){
		//make a class object
		MyTest test=new MyTest();
		
		//save the generated number in trap
		
		while (trap_counter<10){
			test.traps.add(trap_counter, test.generator()) ;
			trap_counter+=1;
			Analyzer analyze=new Analyzer();
			analyze.start();
		}
		//end of main function
	}
	//end of class
}
