import sys
n=int(input())
li=list(map(int,sys.stdin.readline().split(" ")))
a,b=10**9,10**9
l,r=0,n-1

while l<r:
    if abs(li[l]+li[r])<abs(a+b):
        a,b=li[l],li[r]
        if a+b==0:
            break
    if li[l]+li[r]<0:
        l+=1
    elif li[l]+li[r]>0:
        r-=1
print(a,b)