import sys
from collections import deque

input=sys.stdin.readline
n,k=map(int,input().split(" "))
graph=[0]*1000001
q=deque()
q.append((n,0))
while True:
    cur_loc,cur_time=q.popleft()
    if cur_loc==k:
        print(cur_time)
        break
    if cur_loc<=50000 and graph[2*cur_loc]==0:
        graph[cur_loc]=cur_time
        q.append((2*cur_loc,cur_time))
    if cur_loc>0 and graph[cur_loc-1]==0:
        graph[cur_loc-1]=cur_time+1
        q.append((cur_loc-1,cur_time+1))
    if cur_loc<100000 and graph[cur_loc+1]==0:
        graph[cur_loc+1]=cur_time+1
        q.append((cur_loc+1,cur_time+1))