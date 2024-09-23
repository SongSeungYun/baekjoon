import sys
from collections import deque
from copy import deepcopy

input=sys.stdin.readline
n,m=map(int,input().split(" "))

def bfs(i,j,k):
    temp_graph=deepcopy(graph)
    temp_answer=0
    a,b,c=zero[i],zero[j],zero[k]
    temp_graph[a[1]][a[0]]=1
    temp_graph[b[1]][b[0]]=1
    temp_graph[c[1]][c[0]]=1
    q=deque(two)
    while q:
        x,y=q.popleft()
        for ii in range(4):
            nx=x+dx[ii]
            ny=y+dy[ii]
            if 0<=nx<m and 0<=ny<n and temp_graph[ny][nx]==0:
                temp_graph[ny][nx]=2
                q.append((nx,ny))
    for ii in temp_graph:
        temp_answer+=ii.count(0)
    return temp_answer

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split(" "))))
answer=0
zero=[]#빈칸들의 x,y 좌표
two=[]#바이러스시작점의 x,y 좌표
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            zero.append((j,i))
        elif graph[i][j]==2:
            two.append((j,i))

for i in range(len(zero)):
    for j in range(i+1,len(zero)):
        for k in range(j+1,len(zero)):
            answer=max(answer,bfs(i,j,k))
print(answer)