#include <stdio.h>

int main(void){
    int n;
    scanf("%d",&n);
    int cont=0;
    while(n>0){
        if(n%5==0){
            n=n-5;
            cont++;
        }
        else if(n%3==0){
            n=n-3;
            cont++;
        }
        else if(n>=5){
            n=n-5;
            cont++;
        }
        else{
            cont=-1;
            break;
        }
    }
    printf("%d",cont);
    return 0;
}