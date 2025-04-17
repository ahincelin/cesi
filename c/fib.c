
#include <stdio.h>

unsigned long Fib(unsigned long n) {
    unsigned long resultat;
    
    if (n < 2L) {
        resultat = 1L;
    } else {
        resultat = Fib(n - 1) + Fib(n - 2);
    }
    return resultat;
}


int main() {
	printf("Fib(12) :%d\n", Fib(12));
	return 0;
}
