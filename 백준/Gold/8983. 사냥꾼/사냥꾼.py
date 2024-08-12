import sys
input=sys.stdin.readline
m,n,l=map(int,input().split(" "))
sade=sorted(list(map(int,input().split(" "))))
answer=0
for _ in range(n):
    x,y=map(int,input().split(" "))
    left,right=0,m-1
    while left<=right:
        mid=(left+right)//2
        if abs(sade[mid]-x)+y<=l:
            answer+=1
            break
        if sade[mid]<x:
            left=mid+1
        else:
            right=mid-1
print(answer)