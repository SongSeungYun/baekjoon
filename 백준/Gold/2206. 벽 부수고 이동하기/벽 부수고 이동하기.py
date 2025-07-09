import sys
from collections import deque
input=lambda:sys.stdin.readline().strip()
n,m=map(int,input().split(" "))
route=[]
for _ in range(n):
    route.append(input())
q=deque()
q.append((0,0,0,False))#x,y,cost,벽뚫여부
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visited=[[False]*m for _ in range(n)]
visited[0][0]=True
broken_visited=[[False]*m for _ in range(n)]
answer=-1
while q:
    pre_x,pre_y,cost,broke_wall=q.popleft()
    #print(pre_x,pre_y,cost,broke_wall)
    if (pre_x,pre_y)==(m-1,n-1):
        answer=cost+1
        break
    for i in range(4):
        x=pre_x+dx[i]
        y=pre_y+dy[i]
        if 0<=x<m and 0<=y<n:
            if route[y][x]=="0" and not broke_wall and not visited[y][x]:
                q.append((x,y,cost+1,broke_wall))
                visited[y][x]=True
            elif route[y][x]=="0" and broke_wall and not broken_visited[y][x]:
                q.append((x,y,cost+1,broke_wall))
                broken_visited[y][x]=True
            elif route[y][x]=="1" and not broke_wall and not broken_visited[y][x]:
                q.append((x,y,cost+1,True))
                broken_visited[y][x]=True
print(answer)