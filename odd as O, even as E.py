n = int(input())
sum1=0
while n :
    d = n%10
    n //= 10
    sum1 += d
if (sum1%2)==0:
    print('E')
else:
    print('S')
