N=map(int,input())
n=list(N)
length=len(n)
sum=0
for i in n:
    product=i**length
    sum+=product
print(sum)
