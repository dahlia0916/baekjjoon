import sys    
N,K=map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count=0
ans=-1

def merge(arr,p,q,r):
    i=p
    j=q+1
    tmp=[]
    global count,ans
    while(i<=q and j<=r):
        if(arr[i]<=arr[j]):
            tmp.append(arr[i])
            i=i+1
        else:
            tmp.append(arr[j])
            j=j+1
    while(i<=q):
        tmp.append(arr[i])
        i=i+1
    while(j<=r):
        tmp.append(arr[j])
        j=j+1
    i=p
    t=0
    while(i<=r):
        arr[i]=tmp[t]
        count=count+1
        if count==K:
            ans=arr[i]
            break
        i=i+1
        t=t+1


def merge_sort(arr,p,r):
    if(p<r):
        q=(p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

merge_sort(arr,0,N-1)
print(ans)
