#include <stdio.h>

int x[100], y[100], z[100], i;

main() {
    
    while(1) {
        scanf("%d %d %d", &x[i], &y[i], &z[i]);
        
        if (x[i] == 0) break;
        i++;
        
    }
    
    for (int j=0; j<i; j++) {
        if (
			x[j]*x[j] + y[j]*y[j] == z[j]*z[j]
			|| y[j]*y[j] + z[j]*z[j] == x[j]*x[j]
			|| x[j]*x[j] + z[j]*z[j] == y[j]*y[j]) printf("right\n");
        else printf("wrong\n");
    }
    
}