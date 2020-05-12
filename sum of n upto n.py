n=int(input("Enter a number = "))
count=0
for i in range(1,n):
    for j in range(1,n):
        c=(i+j)
        if c==n:
            count+=1
print(count)
