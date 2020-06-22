n=int(input())
N=list(map(int,input().split()))[:n]
print(max(set(N),key=N.count))
