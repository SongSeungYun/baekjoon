t=int(input())
def sol(m,n,x,y):
    m,n,x,y=m,n,x,y
    x-=1
    y-=1
    a=x
    while a<=m*n:
        if a%n==y:
            k=a
            return k+1
        else:
            a+=m
    return -1
for i in range(t):
    m,n,x,y=map(int,input().split(" "))
    print(sol(m,n,x,y))