from collections import deque
import sys
input=lambda:sys.stdin.readline().strip()
k=int(input())
w,h=map(int,input().split(" "))
field=[]
for _ in range(h):
    field.append(list(map(int,input().split(" "))))
q=deque()
q.append((0,0,0,0))#x,y,점프 쓴 횟수,이동 횟수
visited=[[[False]*(k+1) for _ in range(w)] for _ in range(h)]
visited[0][0][0]=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
jump_dx=[-2,-1,1,2,2,1,-1,-2]
jump_dy=[1,2,2,1,-1,-2,-2,-1]
answer=-1
while q:
    x,y,jump_cnt,move_cnt=q.popleft()
    #print((x,y,jump_cnt,move_cnt,visited[y][x]))
    if (x,y)==(w-1,h-1):
        answer=move_cnt
        break
    for i in range(4):
        cur_x=x+dx[i]
        cur_y=y+dy[i]
        if 0<=cur_x<w and 0<=cur_y<h and not visited[cur_y][cur_x][jump_cnt] and field[cur_y][cur_x]==0:
            visited[cur_y][cur_x][jump_cnt]=True
            q.append((cur_x,cur_y,jump_cnt,move_cnt+1))
    if jump_cnt>=k:
        continue
    for i in range(8):
        cur_x=x+jump_dx[i]
        cur_y=y+jump_dy[i]
        if 0<=cur_x<w and 0<=cur_y<h and not visited[cur_y][cur_x][jump_cnt+1] and field[cur_y][cur_x]==0:
            visited[cur_y][cur_x][jump_cnt+1]=True
            q.append((cur_x,cur_y,jump_cnt+1,move_cnt+1))
print(answer)