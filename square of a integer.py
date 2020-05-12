N=int(input())
count=0
if 1<=N<=100000:
    temp=N%10
    count+=(temp*temp)
    temp // 10
print(count)
