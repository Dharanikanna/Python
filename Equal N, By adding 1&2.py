N=int(input())
count=0
if 1<=N<=100000:    
    for i in range (1,3):
        for j in range (1,3):
            for k in range (1,3):
                for l in range (1,3):
                    for m in range (1,3):
                        for n in range (1,3):
                            c=i+j+k+l+m+n
                            if c==N:
                                count+=1
                                print(i,j,k,l,m,n,'-',c,count)
