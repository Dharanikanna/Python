S,X =map(str,input().split())
s=len(S)
x=len(X)
c=s-x
if c==1 or c==-1:
    print('yes')
else:
    print('no')
