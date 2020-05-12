def rotate(S,K): 
	Lfirst = S[0 : K] 
	Lsecond =S[K :] 
	print (Lsecond + Lfirst)
S,K=[str(input()),int(input())]
rotate(S,K) 
