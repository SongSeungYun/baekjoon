import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split(" "))
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split(" "))))
visited=[[0]*m for _ in range(n)]
answer=[[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            answer[i][j]=0
        elif graph[i][j]==2:
            start=(j,i)

q=deque()
q.append((start[0],start[1],0))
visited[start[1]][start[0]]=1
answer[start[1]][start[0]]=0
dx=[1,-1,0,0]
dy=[0,0,-1,1]
while q:
    x,y,distance=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<m and 0<=ny<n and
            graph[ny][nx]==1 and not visited[ny][nx]):
            answer[ny][nx]=distance+1
            q.append((nx,ny,distance+1))
            visited[ny][nx]=1
for i in range(n):
    for j in range(m):
        print(answer[i][j],end=" ")
    print()