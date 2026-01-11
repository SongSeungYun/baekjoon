import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split(" "))
small=[]
for _ in range(m):
    small.append(int(input()))

q=deque()
q.append((2,1,1))#위치, 보폭, 시간
if 2 in small:
    q=deque()
bopoks=[[] for _ in range(n+1)]
bopoks[1]=[1]
if_answer=False
while q:
    x,bopok,time=q.popleft()
    # print(x,bopok,time)
    if x==n:
        if_answer=True
        print(time)
        break
    for dx in [-1,0,1]:
        cur_bopok=bopok+dx
        cur_loc=x+cur_bopok
        if cur_bopok>=1 and 1<cur_loc<=n and cur_bopok not in bopoks[cur_loc] and cur_loc not in small:
            q.append((cur_loc,cur_bopok,time+1))
            bopoks[cur_loc].append(cur_bopok)
if not if_answer:
    print(-1)

'''
23 8
13
14
15
17
18
20
21
22

1 2 4 7 9 12 16 19 23
'''