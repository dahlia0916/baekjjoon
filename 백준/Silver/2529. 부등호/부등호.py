import sys
k=int(sys.stdin.readline())
l=list(map(str,sys.stdin.readline().strip().split()))
v=[0]*(10)

max_sol=""
min_sol=""

def check(i,j,f):
    if f == "<":
        return i<j
    else:
        return i>j

def solve(count,s):
    global max_sol,min_sol
    if count == k+1:
        if len(min_sol)==0:
            min_sol = s
        else:
            max_sol = s
        return
    for i in range(10):
        if v[i]==0:
            if count ==0 or check(s[-1],str(i),l[count-1]):
                v[i]=1
                solve(count+1,s+str(i))
                v[i]=0
solve(0,"")
print(max_sol)
print(min_sol)