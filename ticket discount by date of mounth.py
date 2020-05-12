n = int(input())
L = [int(x) for x in input().split()]
k = int(input())
L2 = []
for x in  L :
    if x%k==0 :
        L2.append(1)
    else :
        L2.append(0)
print(*L2,end='')
