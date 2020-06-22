n=int(input())
m=list(map(int,input().split()))[:n]
c=m[::-1]
for i in c:
	print(i,end=" ")
