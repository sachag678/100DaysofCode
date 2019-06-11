#include <stdio.h>

int factorial(int num){
	int fact = 1;
	for(int i=1;i<num;i=i+1){
	fact = fact*i;
	}
	return fact;
}

void main(void) {}
