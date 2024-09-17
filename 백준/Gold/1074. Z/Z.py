n,r,c=map(int,input().split(" "))
def rec(nn,answer,x,y):
    if nn==1:
        return answer
    else:
        m=nn//2
        if x>=m and y>=m:
            return rec(m,3*m**2+answer,x-m,y-m)
        elif x>=m and y<m:
            return rec(m,m**2+answer,x-m,y)
        elif x<=m and y>=m:
            return rec(m,2*m**2+answer,x,y-m)
        else:
            return rec(m,answer,x,y)
print(rec(2**n,0,c,r))