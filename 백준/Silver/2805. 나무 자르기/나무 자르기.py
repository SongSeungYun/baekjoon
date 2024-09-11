#https://devfunny.tistory.com/674
import sys
n,m=map(int,input().split(" "))
trees = list(map(int,sys.stdin.readline().split()))

start=1
end=max(trees)
while start<=end:
    mid=(start+end)//2
    countt=0
    for tree in trees:
        countt+=max(0,tree-mid)
    if m<=countt:
        start=mid+1
    else:
        end=mid-1
print(start-1)