import sys
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split(" "))))
if graph[n-1][n-1]==1:
    print(0)
    exit(0)
dp=[[0]*(n) for _ in range(n)]
stack=[]
stack.append((0,1,0))#(y좌표, x좌표, 파이프방향)0 가로 1 세로 2 대각선
dx=[1,1,0]
dy=[0,1,1]
while stack:
    y,x,dir=stack.pop()
    if dir!=1 and x<n-1 and graph[y][x+1]==0:
        dp[y][x+1]+=1
        stack.append((y,x+1,0))
    if dir!=0 and y<n-1 and graph[y+1][x]==0:
        dp[y+1][x]+=1
        stack.append((y+1,x,1))
    if  y<n-1 and x<n-1 and sum(graph[y+dy[i]][x+dx[i]] for i in range(3))==0:
        dp[y+1][x+1]+=1
        stack.append((y+1,x+1,2))
print(dp[n-1][n-1])