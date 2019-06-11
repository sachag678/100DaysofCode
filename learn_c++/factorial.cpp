#include <iostream>
#include <chrono>

using namespace std::chrono;

int main(){
    auto start = high_resolution_clock::now();

    unsigned int n = 6;
    unsigned long long sum = 1;
    for(int i=2; i <= n; ++i){
        sum = sum * i;
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
	
    std::cout <<"output : " << sum << std::endl;
    std::cout <<"iterative_factorial : " << duration.count() << std::endl;

    return 0;
}
