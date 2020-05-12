def fdigit(A):
    while (A>=10):
        A=A//10    
    return(A)
#--------------------
def ldigit(A):
    A=A%10
    return(A)
#--------------------
A=int(input())
count=0
print(fdigit(A)+ldigit(A))

