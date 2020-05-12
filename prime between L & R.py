L,R=list(map(int,input().split()))
count=0
if L<=R<=100000:
    for i in range(L,R+1):
        if (i%2)!=0:
            count+=1
    print(count)
