import java.util.ArrayList;
import java.util.List;


class Testing {
	boolean interuppted=false;
	
	public synchronized void analyze(int message){
		// if thread is interrupted, then do something
		if (interuppted){
			try {
				Thread.sleep(1000);
				System.out.println("Hey! look i did something");
			} catch (InterruptedException e){
				System.out.println("Nooo... Exception");
				e.printStackTrace();
			}
		}
		System.out.println("analysis done, waiting for next");
		interuppted=false;
		notify();
	}
	
	public synchronized void query(){
		if (!interuppted){
			try{
				Thread.sleep(1000);
				System.out.println("Something sent to analyze");
			} catch (InterruptedException e){
				System.out.println("lol o gya");
				e.printStackTrace();
			}
		}
		System.out.println("sent for analysis");		
		interuppted=true;
		notify();
	}
}

public class InterThreadComm {
	static List<Integer> abc=new ArrayList<Integer>();
	static List<Integer> cde=new ArrayList<Integer>();
	static int abc_counter=0;
	static int cde_counter=0;
	
	public void main_method(){

		class Analyzer implements Runnable {
			Testing t;
			public Analyzer (Testing t1){
				//constructor
				this.t=t1;
				new Thread().start();
			}
			public synchronized void run(){
				t.analyze(abc.get(abc_counter));
				abc_counter+=1;
			}
		}
	}
}


