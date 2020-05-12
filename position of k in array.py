N,k=map(int,input().split())
n=list(map(int,input().split()))[:N]
b=n.index(k)
count=0
for i in n:
    count=i
    c=count-i
    if (c==1):
        if b>0:
            print(b+1)
        else:
            print(-1)
