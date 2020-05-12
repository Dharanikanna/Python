n = int(input(""))
temp = n
rev = 0
s=0
for i in range(0,n):
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
     	temp = temp // 10
    s=+1
    print(s)
