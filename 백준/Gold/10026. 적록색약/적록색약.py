import sys
from collections import deque

n=int(input())
graph=[sys.stdin.readline().rstrip() for _ in range(n)]
visited=[[0]*n for _ in range(n)]
q=deque()
dx=[1,-1,0,0]
dy=[0,0,-1,1]
answer1,answer2=0,0#적록x,적록o

for i in range(n):#적록x
    for j in range(n):
        if visited[i][j]:
            continue
        answer1+=1
        q.append((i,j))
        visited[i][j]=1
        color=graph[i][j]
        while q:
            y,x=q.popleft()
            for k in range(4):
                cur_x=x+dx[k]
                cur_y=y+dy[k]
                if 0<=cur_x<n and 0<=cur_y<n and not visited[cur_y][cur_x] and graph[cur_y][cur_x]==color:
                    q.append((cur_y,cur_x))
                    visited[cur_y][cur_x]=1

visited=[[0]*n for _ in range(n)]
d={"R":"R","G":"R","B":"B"}
for i in range(n):#적록o
    for j in range(n):
        if visited[i][j]:
            continue
        answer2+=1
        q.append((i,j))
        visited[i][j]=1
        color=d[graph[i][j]]
        while q:
            y,x=q.popleft()
            for k in range(4):
                cur_x=x+dx[k]
                cur_y=y+dy[k]
                if 0<=cur_x<n and 0<=cur_y<n and not visited[cur_y][cur_x] and d[graph[cur_y][cur_x]]==color:
                    q.append((cur_y,cur_x))
                    visited[cur_y][cur_x]=1

print(answer1,answer2)