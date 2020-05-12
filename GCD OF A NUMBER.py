N=int(input())
M=int(input())
if N>M:
    for i in range (1,M+1):
        if (N%i==0) and (M%i==0):
            c=i
    print(c)
else:
    for i in range (1,N+1):
        if (N%i==0) and (M%i==0):
            c=i
    print(c)