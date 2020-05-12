N =int(input())
temp=0
temp=N%10
if temp%2!=0 :
    for i in range(temp):
        print(i)
        temp//10
else:
    print(-1)
