'''
1.Find Arasu Numbers using python    
'''
    Arasu numer series is nothing but Adding 1 in square of digit
    eg: 1*1=1 --> 1+1=2, 2*2=1 --> 4+1=5

n=int(input())
for i in range(1,n+1):
	print((i**2)+1,end=' ')
