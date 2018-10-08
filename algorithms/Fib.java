import java.util.Arrays;

class Fib{

	public int fib_recursive(int n, int ... memory){
		
		if(memory.length==0){
			memory = new int[n];
		}

		if(n==0 || n==1){
			return n;
		}

		if(memory[n-1]==0){
			memory[n-1] = fib_recursive(n - 1, memory) + fib_recursive(n -2 , memory);
		}

		return memory[n-1];
	}

	public static void main(String [] args){
		Fib fib = new Fib();
		System.out.println(fib.fib_recursive(10));
		}

}
