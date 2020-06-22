'''
You are given with an array. For each element present in 
the array your task is to print the next smallest than that number. If it is not smallest print -1

inputs:
7
10 7 9 3 2 1 15
'''

n=int(input())
m=list(map(int,input().split()))[:n]
d=[]
for i in range (len(m)):
    for j in m:
        if (m[i]< j):
            continue
        elif (m[i]> j) and (i<m.index(j)):
            d.append(j)
            break
        elif (m[i]==(m[-2])):
            if m[-1]> m[-2]:
                d.append(-1)
        elif (m[i]==m[-1]):
            d.append(-1)
            break
print (d)
