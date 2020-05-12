N=int(input())
num=1
while N>0 and N<100000000000:
    num*=N%10
    N=N // 10
print(num)
