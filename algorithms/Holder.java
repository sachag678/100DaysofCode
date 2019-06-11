import java.util.Objects;

class Holder{

	public int num1;
	public int num2;

	public Holder(int i, int j){
		num1 = i;
		num2 = j;
	}

	@Override
	public int hashCode(){
		return Objects.hash(num1, num2);
	}
	
	@Override
	public boolean equals(Object obj){
		Holder holder = (Holder) obj;
		return holder.num1 == this.num1 && holder.num2 == this.num2;
	}

	@Override
	public String toString(){
		return "(" + num1 + ", " + num2 + ")";
	}
	


}
