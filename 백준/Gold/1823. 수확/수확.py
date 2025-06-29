n=int(input())

rice=[0]
for i in range(n):
    rice.append(int(input()))

bubunhap=[0]*(n+1)
for i in range(1,n+1):
    bubunhap[i]=bubunhap[i-1]+rice[i]
def hap(n,m):
    return bubunhap[m]-bubunhap[n-1]

dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i]=rice[i]
for i in range(1,n):
    for j in range(1,n-i+1):
        dp[j][j+i]=hap(j,j+i)+max(dp[j][j+i-1],dp[j+1][j+i])

print(dp[1][n])