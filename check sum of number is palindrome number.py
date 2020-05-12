N = int(input())
sum1=0
while 2<=N<=1000000000000000000:
    d = N%10
    N //= 10
    sum1 += d
rev = ''.join(reversed(str(sum1)))
if (str(sum1) == rev):
    print('yes') 
else:
    print('no')
