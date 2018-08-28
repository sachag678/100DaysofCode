import java.util.ArrayList;

public class PowerSet{

	public ArrayList<ArrayList<Integer>> getSubsets(ArrayList<Integer> set,  int index){
		ArrayList<ArrayList<Integer>> allsubsets;

		if(set.size() == index){
			allsubsets = new ArrayList<ArrayList<Integer>>();
			allsubsets.add(new ArrayList<Integer>());
		}else{
			allsubsets = getSubsets(set, index + 1);
			int item = set.get(index);
			ArrayList<ArrayList<Integer>> moresubsets = new ArrayList<ArrayList<Integer>>();
			for (ArrayList<Integer> subset: allsubsets){
				ArrayList<Integer> newsubset = new ArrayList<Integer>();
				newsubset.addAll(subset);
				newsubset.add(item);
				moresubsets.add(newsubset);
			}
			allsubsets.addAll(moresubsets);
		}
		return allsubsets;
	}

	public static void main(String[] args){
		ArrayList<Integer> set = new ArrayList<Integer>();
		for(int i=1;i<3;i++){
			set.add(i);
		}
		PowerSet powerset = new PowerSet();
		ArrayList<ArrayList<Integer>> pset = powerset.getSubsets(set, 0);
		System.out.println(pset.toString());

	}
}
