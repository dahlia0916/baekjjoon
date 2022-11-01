#include <stdio.h>

int main() {
    int n,coin,cnt,max_c;
    int sol=0;
    scanf("%d %d",&n,&coin);
    int A[n];
    for (int i=0;i<n;i++){
        scanf("%d",&cnt);
        A[i]=cnt;
    }
    if(A[n-1]<=coin){
        max_c=n-1;
    }
    else{
        for (int l=n;l>0;l--){
            if(A[l]>coin){
                max_c=l;
                break;
            }
        }
    }

    for (int k=max_c;k>0;k--){
        while(A[k]<=coin){
            coin=coin-A[k];
            sol++;
        }
    }
    if (coin != 0){
        sol=sol+coin;
    }
    printf("%d",sol);
    return 0;
}