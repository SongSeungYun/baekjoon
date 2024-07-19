import sys
n=int(input())
l=[0]+list(map(int,sys.stdin.readline().split(" ")))
dp=[[0]*(n+1) for _ in range(n+1)]
dp[1][1]=1
for i in range(2,n+1):
    j=i//2-1
    while j>=0 and l[1+j]==l[i-j]:
        dp[1+j][i-j]=1
        j-=1
    while j>=0:
        dp[1+j][i-j]=0
        j-=1
for i in range(2,n):
    dp[i][i]=1
    j=(n-i+1)//2-1
    while j>=0 and l[i+j]==l[n-j]:
        dp[i+j][n-j]=1
        j-=1
    while j>=0:
        dp[i+j][n-j]=0
        j-=1
dp[n][n]=1
m=int(input())
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split(" "))
    print(dp[a][b])