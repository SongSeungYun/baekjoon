import sys
n=int(input())
ns=list(map(int,sys.stdin.readline().strip().split()))
m=int(input())
ms=list(map(int,sys.stdin.readline().strip().split()))
ns.sort()
for num in ms:
    left=0
    right=n-1
    answer=0
    while left<=right:
        mid=(left+right)//2
        if ns[mid]<num:
            left=mid+1
        elif num<ns[mid]:
            right=mid-1
        else:
            answer=1
            break
    print(answer, end=" ")