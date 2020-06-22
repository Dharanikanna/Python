'''
5.Given a string as input, you have to reverse the string
    by keeping the punctuation and spaces intact. 
    You have to modify the source string itself without creating another string.
'''

N=input()
n=list(N)
i=0
j=len(n)-1
while i<j:
    if not n[i].isalpha():
        i+=1    
    elif not n[j].isalpha():
        j-=1
    else:
        n[i],n[j]=n[j], n[i]
        i+=1
        j-=1
strOut=''.join(n)
print(strOut)
