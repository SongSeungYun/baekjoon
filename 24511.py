from collections import deque
import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
bb=list(map(int,sys.stdin.readline().split()))
b=deque()
for i in range(len(a)):
    if a[i]==0:
        b.appendleft(bb[i])
m=int(input())
c=deque(map(int,sys.stdin.readline().split()))
b.extend(c)
for i in range(m):
    print(b[i],end=" ")

'''
6
0 0
1 2
6
3 4 5 6 7 8

2 1 3 4

3 1
1 2

4 3
3 1

5 4
4 3

6 5
5 4




'''