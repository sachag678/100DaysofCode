#include <iostream>
#include <chrono>

using namespace std::chrono;
using namespace std;

int main(){
	int target = 5567393;
	int num = 10000000;
	int* prime= new int[num];
	for(int i =0;i<num;++i)
	    prime[i] = i;

    	auto start = high_resolution_clock::now();
	int min = 0;
	int max = num;
	int guess = (min + max)/2;
	while(prime[guess] != target){
		if(min >= max){
		    return 0;
		}
		if(prime[guess]<target){
		    min = guess + 1;
		}else{
		    max = guess - 1;
		}
		guess = (min + max)/2;
	}
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<nanoseconds>(stop - start);
	
        cout <<"output : " << guess << endl;
        cout <<"iterative_factorial : " << duration.count() << endl;

	return 0;


}
