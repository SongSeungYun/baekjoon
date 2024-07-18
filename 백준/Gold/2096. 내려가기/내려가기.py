n=int(input())
max_dp=[[0,0,0] for _ in range(n)]
min_dp=[[0,0,0] for _ in range(n)]
temp=list(map(int,input().split(" ")))
max_dp[0]=temp
min_dp[0]=temp
for i in range(1,n):
    temp=list(map(int,input().split(" ")))
    max_dp[i][0]=temp[0]+max(max_dp[i-1][0],max_dp[i-1][1])
    min_dp[i][0]=temp[0]+min(min_dp[i-1][0],min_dp[i-1][1])
    max_dp[i][1]=temp[1]+max(max_dp[i-1])
    min_dp[i][1]=temp[1]+min(min_dp[i-1])
    max_dp[i][2]=temp[2]+max(max_dp[i-1][1],max_dp[i-1][2])
    min_dp[i][2]=temp[2]+min(min_dp[i-1][1],min_dp[i-1][2])
print(max(max_dp[n-1]),min(min_dp[n-1]))