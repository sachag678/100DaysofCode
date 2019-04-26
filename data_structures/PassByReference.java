public class PassByReference{

	public void change(Person person){
		person = new Person("john", 23);
	}	

	public static void main(String [] args){
		
		Person person = new Person("Jake", 34);
		System.out.println(person.toString());
		
		PassByReference pf = new PassByReference();
		pf.change(person);
		
		System.out.println(person.toString());
	}

}
