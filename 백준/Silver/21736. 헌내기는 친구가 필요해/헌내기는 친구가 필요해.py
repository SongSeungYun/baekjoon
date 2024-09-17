import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split(" "))
graph=[]
for _ in range(n):
    graph.append(input())
visited=[[0]*m for _ in range(n)]
answer=0

for i in range(n):
    for j in range(m):
        if graph[i][j]=="I":
            start=(j,i)

q=deque()
q.append((start))
visited[start[1]][start[0]]=1
dx=[1,-1,0,0]
dy=[0,0,-1,1]
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
            if graph[ny][nx]=="O":
                q.append((nx,ny))
                visited[ny][nx]=1
            elif graph[ny][nx]=="P":
                q.append((nx,ny))
                visited[ny][nx]=1
                answer+=1
if answer:
    print(answer)
else:
    print("TT")