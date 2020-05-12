n = int(input())
L = [2]
k = 3
for i in range(1,n) :
    L.append(L[i-1] + k)
    k += 2
print(*L,end='')
