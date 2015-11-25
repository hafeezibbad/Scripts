import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

/**
 * This class was written (as a proof of concept) to build and test function calculating difference between two maps and values changed between maps
 * @author eb
 * @date 29-05-2015
 */

public class CalculateMapDifference {

	// (Tentatively) Remove no argument constructor
	public CalculateMapDifference(){
		// Do Nothing
	}
	
	/**
	 * This function takes two (HashMaps) maps as input and returns a (HashMap) map containing key/values pairs which are present in map1 but removed in map2 
	 * @param map1
	 * @param map2
	 * @return map containing values which exist in map2 but not in map1
	 */
	public Map<Integer, String> calcAddedValues(Map<Integer,String> map1, Map<Integer,String> map2){
		Map <Integer,String> addedValues = new ConcurrentHashMap<Integer, String>();
		//Get keysets for maps
		Set <Integer> m1_keySet = map1.keySet();
		Set <Integer> m2_keySet = map2.keySet();
		
		for (int key : m2_keySet){
			// if map1 does not have the key, its an addition
			if (!map1.keySet().contains(key)){
				addedValues.put(key, map2.get(key));
			}
		}
		return addedValues;
	}
	
	/**
	 * This function takes two (HashMaps) maps as input and returns a (HashMap) map containing key/values pairs which are present in map1 but removed in map2 
	 * @param map1
	 * @param map2
	 * @return map containing values which exist in map1 but not in map2
	 */
	public Map<Integer, String> calcRemovedValues(Map<Integer,String> map1, Map<Integer,String> map2){
		Map <Integer,String> removedValues = new ConcurrentHashMap<Integer, String>();
		//Get keysets for maps
		Set <Integer> m1_keySet = map1.keySet();
		Set <Integer> m2_keySet = map2.keySet(); 
		for (int key : m1_keySet){
			// if map1 does not have the key, its an addition
			if (!(m2_keySet.contains(key))){
				removedValues.put(key, map1.get(key));
			}
		}
		return removedValues;
	}
	
	/**
	 * This function takes two (HashMaps) maps as input and returns a (HashMap) map containing key/values pairs which are changed from map1 to map2 
	 * @param map1
	 * @param map2
	 * @return map containing keys (from map1) and changed values
	 */
	
	public Map<Integer, String> calcChangedValues(Map<Integer,String> map1, Map<Integer,String> map2){
		Map <Integer,String> changedValues = new ConcurrentHashMap<Integer, String>();
		//Get keysets for maps
		Set <Integer> m1_keySet = map1.keySet();
		Set <Integer> m2_keySet = map2.keySet();
		for (int key : m1_keySet){
			// if map1 does not have the key, its an addition
			if (m2_keySet.contains(key) && !map2.get(key).equals(map1.get(key))){
				changedValues.put(key, map2.get(key));
			}
		}
		return changedValues;
	}
	
	/**
	 * Test function for calcAddedValues function
	 */
	public void testAddedValues(){
		Map <Integer, String> m1 = new ConcurrentHashMap <Integer, String>();
		Map <Integer, String> m2 = new ConcurrentHashMap <Integer, String>();
		Map <Integer,String> m4;
		// populate the map
		for (int i=1;i<10;i++){
			m1.put(i,Integer.toString(i));
		}
		// make another map
		for (int i=1;i<18;i++){
			m2.put(i,Integer.toString(i));
		}
		// calculate the added values in new map
		m4 = calcAddedValues(m1, m2);
		// display results
		if (m4.isEmpty()){
			System.out.println("No new values added");
		} else {
			System.out.println("Added values are ");
			for (int key: m4.keySet()){
				System.out.println(key+", "+m4.get(key));
			}
		}
	}
	
	/**
	 * Test function for calcRemovedValues function
	 */
	public void testRemovedValues(){
		Map <Integer, String> m1 = new ConcurrentHashMap <Integer, String>();
		Map <Integer, String> m2 = new ConcurrentHashMap <Integer, String>();
		Map <Integer,String> m4;
		// populate the map
		for (int i=1;i<15;i++){
			m1.put(i,Integer.toString(i));
		}
		// make copy
		m2.putAll(m1);
		Set<Integer> m2keys = m2.keySet();
		// remove some values from copy
		for (int key: m2keys){
			if (key > 10){
				m2.remove(key);
			}
		}
	    // calculate values removed in copy	
		m4 = calcRemovedValues(m1, m2);
		// display results
		if (m4.isEmpty()){
			System.out.println("No values removed");
		} else {
			System.out.println("Removed values are ");
			for (int key: m4.keySet()){
				System.out.println(key+", "+m4.get(key));
			}
		}
	}

	/**
	 * Test function for calcChangedValues function
	 */
	public void testChangedValues(){
		Map <Integer, String> m1 = new ConcurrentHashMap <Integer, String>();
		Map <Integer, String> m2 = new ConcurrentHashMap <Integer, String>();
		Map <Integer,String> m4;
		// populate the map
		for (int i=1;i<15;i++){
			m1.put(i,Integer.toString(i));
		}
		// make copy
		m2.putAll(m1);
		Set<Integer> m2keys = m2.keySet();
		// changes some values in copy
		for (int key: m2keys){
			if (key > 10){
				m2.put(key,String.valueOf(key*10));
			}
		}
		// calculate changed values in map and copy
		m4 = calcChangedValues(m1, m2);
		// display results
		if (m4.isEmpty()){
			System.out.println("No values changed");
		} else {
			System.out.println("Changed values are ");
			for (int key: m4.keySet()){
				System.out.println("key "+key+": changed value from "+m1.get(key)+" to "+m4.get(key));
			}
		}
	}

	/**
	 * Main Function
	 * @param args
	 */
	
	public static void main (String [] args){
		CalculateMapDifference calcDiff = new CalculateMapDifference();
		calcDiff.testRemovedValues();
		calcDiff.testAddedValues();
		calcDiff.testChangedValues();
		
	}
}
