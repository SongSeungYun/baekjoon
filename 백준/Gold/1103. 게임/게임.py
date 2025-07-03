n,m=map(int,input().split(" "))
board=[]
for i in range(n):
    board.append(list(input()))
for i in range(n):
    for j in range(m):
        if board[i][j]=="H":
            board[i][j]=-1
        else:
            board[i][j]=int(board[i][j])

answer=1
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visited=[[False]*m for _ in range(n)]
dp=[[0]*m for _ in range(n)]

def dfs(cnt,x,y):
    global answer,dx,dy,board,visited
    if not (0<=x<m and 0<=y<n) or board[y][x]==-1:
        global answer
        answer=max(answer,cnt-1)
        return
    elif visited[y][x]:
        print(-1)
        exit()
    if dp[y][x]>=cnt:
        return
    else:
        dp[y][x]=cnt
    visited[y][x]=True
    for i in range(4):
        dfs(cnt+1,x+board[y][x]*dx[i],y+board[y][x]*dy[i])
    visited[y][x]=False
dfs(1,0,0)
print(answer)