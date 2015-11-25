package testing;

public class Testing {

	public static void main (String[] args){
		TestClass t1 = new TestClass();
		TestClass2 t2 = new TestClass2();
		
		t1.display();
		//Permanently changes the Map object of T1 in T2
//		t2.doViaCopy(t1.myMap);
		// Does not permanently changes the Map object of T1 in T2
		t2.doViaPut(t1.myMap);
		
	}
}
