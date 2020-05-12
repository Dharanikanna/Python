import math
N=int(input())
def Log2(x): 
    return (math.log10(x) / 
            math.log10(2));
def isPowerOfTwo(n): 
    return (math.ceil(Log2(N)) == math.floor(Log2(N)));  
if(isPowerOfTwo(N)): 
    print("Yes"); 
else: 
    print("No");
    
