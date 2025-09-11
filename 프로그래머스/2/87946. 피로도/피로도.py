def solution(k, dungeons):
    def swap(inn,out):
        temp=input[inn]
        input[inn]=input[out]
        input[out]=temp

    def permutation(depth):
        if depth==N:
            tk=k
            result=0
            for t in range(len(input)):
                if input[t][0]<=tk and t==(len(input)-1):
                    result=result+1
                    results.append(result)
                elif input[t][0]<=tk:
                    tk=tk-input[t][1]
                    result=result+1
                else:
                    results.append(result)
                    break
            return 
        for i in range(depth,N):
            swap(i,depth)
            permutation(depth+1)
            swap(i,depth)

    N=len(dungeons)
    input=dungeons
    results=[]
    permutation(0)
    return max(results)