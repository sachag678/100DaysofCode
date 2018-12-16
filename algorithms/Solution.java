import java.util.Arrays;
/**
 * Implement a function that finds the Nth Order Statistic.
 * It is the Nth Smallest value in an ordered array.
 * [10, 2, 6, 5, 9, 3, 15] finds the 3rd order statistic => 6
 * Uses a Modified version of quicksort.
 */
class Solution{

	public static void main(String [] args){
		int [] input = {10, 2, 6, 5, 9, 3, 15};
		System.out.println(NthSmallest(input, 3, 0, input.length-1));
		System.out.println(Arrays.toString(input));
	}

	/**
	 * Uses the partiallySortedArray() function to get the pivot point.
	 * Uses the pivot point to determine which portion of the array to sort partition next.
	 * Does this in O(nlog(n))  
	 */
	public static int NthSmallest(int [] arr, int n, int start, int end){
		System.out.println(Arrays.toString(arr));
		int pivot =  PartiallySortedArray(arr, start, end);
		if(n == pivot){
			return pivot;
		}else if(n > pivot){
			return NthSmallest(arr, n, pivot+1, end);
		}else{
			return NthSmallest(arr, n, start, pivot);
		}
	}

	/**
	 * Starts the Pivot at the starting point.
	 * and shifts it until all the elements to its left are smaller and all the 
	 * elements on the right are larger. Returns the pivot point.
	 * Sorts the array in place.
	 */
	public static int PartiallySortedArray(int [] arr, int start, int end){
	
		int pivot = arr[start];
		int i = start;
		int swapped_pos = 0;
		for(int j = start; j < end; j++){
			if(arr[j]<pivot){
				if(i!=j){
					int temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
					swapped_pos = j;
				}
				i = i + 1;
			}
		}
		if(swapped_pos != 0){
			int temp = arr[swapped_pos];
			arr[swapped_pos] = arr[i];
			arr[i] = temp;
		}
		
		return i;
	
	}
}
