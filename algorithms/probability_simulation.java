import java.util.Random;

class Simulation{

	public double calculate(int length){
		int total_two_count = 0;
		for(int k=0;k<length;k++){
		int two_count = 0;
		for(int i = 0; i < 16; i++){
			int student =0;
			for(int j=0; j< 3;j++){
				student += choose();
			}
			if(student==2){
				two_count += 1;
			}
		}
		total_two_count += two_count;
		}

		return total_two_count/(double) length;

	}

	public int choose(){
		Random rand = new Random();
		int ran = rand.nextInt(8);
		if (ran > 4) { return 0; }
		else { return 1; }
	}

	public static void main(String [] args){
	
		Simulation sim = new Simulation();
		System.out.println(sim.calculate(10000000));
	
	}


}
