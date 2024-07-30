import sys
n=int(input())
li=list(map(int,sys.stdin.readline().split(" ")))
a,b=10**9,10**9
for i in range(n-1):
    target=-li[i]
    l=i+1
    r=n-1
    while l<=r:
        mid=(l+r)//2
        if target==li[mid]:
            a,b=li[i],-li[i]
            break
        elif target<li[mid]:
            r=mid-1
        else:
            l=mid+1
    if i<l<n and abs(li[i]+li[l])<abs(a+b):
        a,b=li[i],li[l]
    if i<r<n and abs(li[i]+li[r])<abs(a+b):
        a,b=li[i],li[r]
print(a,b)