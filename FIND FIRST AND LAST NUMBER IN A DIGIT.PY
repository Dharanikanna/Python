def fdigit(A):
    while (A>=10):
        A=A//10    
    print(A)
#--------------------
def ldigit(A):
    A=A%10
    print(A)
#--------------------
A=int(input())
count=0
fdigit(A)
ldigit(A)

