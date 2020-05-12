A,B,C=map(int,input().split())
if A<=100000 and B<=100000 and C<=10000:
    a=A**2
    b=B**2
    c=C**2
    if c==a+b:
        print('yes')
    else:
        print('no')
