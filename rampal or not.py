N=int(input())
sum1=0
while N:
    d = N%10
    N //= 10
    sum1 += d
if (sum1%4)==0:
    print('rampal')
else:
    print('no')
