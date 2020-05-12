n = int(input("Enter length of digit = "))
L = [int(x) for x in input("Enter digits in list method = ").split()]
for i in range(0,n-1,2) :
    L[i],L[i+1] = L[i+1], L[i]
print(*L,end='')
