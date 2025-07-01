from collections import deque
m,n=map(int,input().split(" "))
mapp=[input() for _ in range(n)]
def bfs():
    log=[[-1]*m for _ in range(n)]
    q=deque()#x,y,t(부신벽돌)
    q.appendleft([0,0,0])
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    while q:
        x,y,t=q.pop()
        if t>=log[y][x] and log[y][x]!=-1:
            continue
        log[y][x]=t
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<m and 0<=cy<n:
                q.appendleft([cx,cy,t+int(mapp[cy][cx])])
    return log[n-1][m-1]
print(bfs())