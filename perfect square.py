import math
N,M = map(int,input().split())
number=N*M
root = math.sqrt(number)
if root == N and root == M:
    print('yes')
else:
    print('no')
