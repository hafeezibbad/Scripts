package testing;

import java.util.HashMap;
import java.util.Map;

public class TestClass2 {

	Map <Integer, Integer> myOtherMap= null;
	public TestClass2(){
		// TODO
		myOtherMap = new HashMap<Integer, Integer>();
	}
	
	public void doViaCopy(Map<Integer,Integer> map){
		System.out.println("in doViaCopy Function");
		//copy the map
		myOtherMap = map;
		System.out.println("Displaying my Map");
		display(map); 
		myOtherMap.clear();
		System.out.println("Map cleared");
		System.out.println("Displaying again Map");
		display(map); 
	}
	
	public void doViaPut(Map<Integer,Integer> map){
		System.out.println("in doViaPut Function");
		//put the map
		myOtherMap.putAll(map);
		System.out.println("Displaying my Map");
		display(map); 
		myOtherMap.clear();
		System.out.println("Map cleared");
		System.out.println("Displaying again Map");
		display(map); 
	}
	
	public void display(Map<Integer,Integer> mapi){
		if (mapi.isEmpty() || mapi == null){
			System.out.println("Map is empty");
		}else {
			System.out.println("Map values are");
			for (int key: mapi.keySet()){
				System.out.println(key+":"+mapi.get(key));
			}
		}
	}
}
