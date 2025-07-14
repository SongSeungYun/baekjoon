from collections import deque
import sys
input=lambda:sys.stdin.readline().strip()
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split(" "))))
dx=[1,-1,0,0]
dy=[0,0,-1, 1]

#섬 구분짓기
visited=[[False]*n for _ in range(n)]
island_index=1
for i in range(n):
    for j in range(n):
        if visited[i][j] or graph[i][j]==0:
            continue
        visited[i][j]=True
        graph[i][j]=island_index
        q=deque()
        q.append((j,i))
        while q:
            x,y=q.popleft()
            for k in range(4):
                cur_x=x+dx[k]
                cur_y=y+dy[k]
                if 0<=cur_x<n and 0<=cur_y<n and \
                    graph[cur_y][cur_x]!=0 and not visited[cur_y][cur_x]:

                    q.append((cur_x,cur_y))
                    visited[cur_y][cur_x]=True
                    graph[cur_y][cur_x]=island_index
        island_index+=1

#다리 최소값 찾기
answer=201
for i in range(n):
    for j in range(n):
        make_bridge=False
        for k in range(4):
            cur_x=j+dx[k]
            cur_y=i+dy[k]
            if 0<=cur_x<n and 0<=cur_y<n and graph[i][j]!=0 and graph[cur_y][cur_x]==0:
                make_bridge=True
                break
        if not make_bridge:
            continue
        #print(j,i)
        visited=[[False]*n for _ in range(n)]
        q=deque()
        q.append((j,i,0))#x,y,다리 길이
        get_answer=False
        island=graph[i][j]
        while q:
            x,y,cost=q.popleft()
            for k in range(4):
                cur_x=x+dx[k]
                cur_y=y+dy[k]
                if 0<=cur_x<n and 0<=cur_y<n and not visited[cur_y][cur_x]:
                    if graph[cur_y][cur_x]==0:
                        q.append((cur_x,cur_y,cost+1))
                        visited[cur_y][cur_x]=True
                    elif graph[cur_y][cur_x]!=0 and island!=graph[cur_y][cur_x]:
                        answer=min(answer,cost)
                        get_answer=True
                        break
            if get_answer:
                break
print(answer)
'''
5
1 0 0 0 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
'''