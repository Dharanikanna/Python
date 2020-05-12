N = int(input())
n = list(map(int,input().split()))[:N]
def a(n):
    for x in n :
        if x < N :
            count=0
            count=+1
    return count
def b(n):
    for x in n :
        if x >= N :
            count1=0
            count1=+1
    return count1


print(a(n))
print(b(n))
#if a(n) > b(n):
    # print(x,end=' ')
#else:
   # print('-1')
