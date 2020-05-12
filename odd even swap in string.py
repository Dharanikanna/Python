s=input()
st=list(s)
for i in range(0,len(s),2):
    t=st[i]
    st=st[c+1]
    st[c+1]=t
    return"".join(s)
