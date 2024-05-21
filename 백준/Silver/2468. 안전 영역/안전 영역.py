from collections import deque
n=int(input())
maps=[]
for _ in range(n):
    maps.append(list(map(int,input().split(" "))))


answer=1
dx=[1,-1,0,0]
dy=[0,0,-1,1]

for num in range(0,101):
    temp_answer=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and maps[i][j]>num:
                temp_answer+=1
                q=deque([[i,j]])
                visited[i][j]=1
                while q:
                    y,x=q.popleft()
                    for k in range(4):
                        cur_x=x+dx[k]
                        cur_y=y+dy[k]
                        if 0<=cur_x<n and 0<=cur_y<n and not visited[cur_y][cur_x] and maps[cur_y][cur_x]>num:
                            q.append([cur_y,cur_x])
                            visited[cur_y][cur_x]=1
            answer=max(answer,temp_answer)
print(answer)