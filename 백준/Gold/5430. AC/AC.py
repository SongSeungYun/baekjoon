import sys
input=sys.stdin.readline
from collections import deque
t=int(input())

for _ in range(t):
    p=input().strip()
    n=int(input())
    if_reverse=0
    if_error=0
    if n!=0:
        nums=deque(list(input().strip()[1:-1].split(",")))
    else:
        input()
        nums=[]
    for func in p:
        if func=="R":
            if_reverse=1-if_reverse
        elif len(nums)==0:
            if_error=1
            break
        elif if_reverse:
            nums.pop()
        else:
            nums.popleft()
    if if_error:
        print("error")
        continue
    if if_reverse:
        print("["+",".join(list(nums)[::-1])+"]")
    else:
        print("["+",".join(list(nums))+"]")