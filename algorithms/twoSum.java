import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

class twoSum{
	public int[] calc(int [] nums, int target){
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		for(int i = 0; i< nums.length; map.put(nums[i], i++)){
			if(map.containsKey(target-nums[i])){
				return new int[] {map.get(target-nums[i]), i};
			}
		}
		return new int[] {0, 0};
	}

	public static void main(String [] args){
	twoSum ts = new twoSum();

	System.out.println(Arrays.toString(ts.calc(new int[] {2, 7, 9, 11}, 9)));
	}
}
