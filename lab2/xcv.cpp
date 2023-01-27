#include <stdio.h>
main(){
	int p=1;
	int t=2;
	for(int i=1; i<=2;i++){
		for(int j=1; j<=i;j++){
			t=t*i;
			p=p-t+j;
		}
	}
	printf("%d",p-t);
	return 0;
	
}
