n = int(input())
sum1=0
while n :
    d = n%10
    n //= 10
    sum1 += d*d
print(sum1,end='')
