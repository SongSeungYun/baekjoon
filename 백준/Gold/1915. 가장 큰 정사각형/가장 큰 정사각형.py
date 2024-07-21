import sys
n,m=map(int,input().split(" "))
graph=[list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
max_answer=0
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i-1][j-1]:
            dp[i][j]=(min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])**0.5+1)**2
            max_answer=max(max_answer,dp[i][j])
print(int(max_answer))