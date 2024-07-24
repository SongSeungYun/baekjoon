n=int(input())
l=list(map(int,input().split(" ")))
dp=[[0]*(n-1) for _ in range(21)]
dp[l[0]][0]=1
for i in range(1,n-1):
    for j in range(21):
        if dp[j][i-1] and j+l[i]<=20:
            dp[j+l[i]][i]+=dp[j][i-1]
        if dp[j][i-1] and j-l[i]>=0:
            dp[j-l[i]][i]+=dp[j][i-1]
print(dp[l[-1]][-1])