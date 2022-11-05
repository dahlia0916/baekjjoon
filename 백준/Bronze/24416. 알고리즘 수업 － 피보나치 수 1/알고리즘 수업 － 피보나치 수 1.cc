#include <stdio.h>

int fib(int n) {
    if (n == 1 || n == 2)
     return 1;  //코드1
    else {
        return (fib(n - 1) + fib(n - 2));
    } 
}

// int fibonacci(int n) {
//     int f[n];
//     f[1]=1;
//     f[2]=1;
//     for (int i=3;i<n;i++){
//         f[i] = f[i - 1] + f[i - 2];  //코드2
//     }  
//     return f[n];
// }
int main(){
    int n;
scanf("%d",&n);
int n1=fib(n);
printf("%d\n",n1);
printf("%d\n",n-2);
return 0;
}