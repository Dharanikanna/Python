N=map(int,input())
n=list(N)
maximum=(max(n))
minimum=(min(n))
for i in range (maximum,minimum-1,-1):
    if i!=list(N):
        print(i,end="")
