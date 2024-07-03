import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split(" "))
def solution(nums,l):
    if l==m:
        print(" ".join(map(str,nums)))
        return
    for j in range(nums[-1],n+1):
        solution(nums+[j],l+1)
for i in range(1,n+1):
    solution([i],1)