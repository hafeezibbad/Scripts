import java.io.IOException;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.Scanner;

public class GetMACAddress{

	private static final String ARP_GET_IP_HW = "arp -a";

	public String getARPTable(String cmd) throws IOException {
	           Scanner s = new Scanner(Runtime.getRuntime().exec(cmd).getInputStream()).useDelimiter("\\A");
	                return s.hasNext() ? s.next() : "";
	    }
	
   public static void main(String[] args) throws IOException{

	   GetMACAddress app = new GetMACAddress();
	   System.out.println(app.getARPTable(ARP_GET_IP_HW ));
   }

}
