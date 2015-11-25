package testing;

import java.util.HashMap;
import java.util.Map;

public class TestClass {

	Map <Integer, Integer> myMap = null;
	
	public TestClass (){
		myMap = new HashMap<Integer,Integer>();
		for (int i =0; i< 5; i++){
			myMap.put(i,i);
		}
	}
	
	public void display(){
		if (myMap.isEmpty() || myMap == null){
			System.out.println("Map is empty");
		}else {
			System.out.println("Map values are");
			for (int key: myMap.keySet()){
				System.out.println(key+":"+myMap.get(key));
			}
		}
	}
}
