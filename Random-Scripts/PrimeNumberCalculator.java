import java.util.Timer;
import java.util.TimerTask;

public class calculatePrimesUsingTimer extends Thread {
	public static final int MAX_PRIMES=100000;
	public static final int TEN_SECONDS=10000;
	
	public volatile boolean finished = false;
	public void run () {
		int [] primes= new int [MAX_PRIMES];
		int count=0;
		
		for (int i=2;count<MAX_PRIMES;i++){
			if (finished){
				break;
			}
			boolean prime=true;
			for (int j=0;j<count;j++){
				if (i%primes[j]==0){
					prime=false;
					break;
				}
			}
			if (prime){
				primes[count++]=i;
				System.out.println("Prime Found: "+i);
			}
		}
	}
	
	public static void main (String[] args){
		//make the timer 
		Timer timer = new Timer();
		Timer timer1 = new Timer();
		//needs to be final here... why??
		final calculatePrimesUsingTimer calculate= new calculatePrimesUsingTimer();
		calculate.start();

		timer.schedule(new TimerTask() {
			
			@Override
			public void run() {
				for (int i=0;i<100;i++){
					System.out.println("Hailo");
					
				}
				calculate.finished=true;		
			}
		}, 10000);
		
	}
}
