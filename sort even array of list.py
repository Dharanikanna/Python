n=int(input())
a= list(map(int,input().split()))[:n]
even=[]
for i in range(n):
    if ((i%2)==0):
        even.append(i)
print(even)
