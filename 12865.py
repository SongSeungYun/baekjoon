n,k=list(map(int,input().split(" ")))
w=[]
v=[]
for _ in range(n):
    ww,vv=list(map(int,input().split(" ")))
    w.append(ww)
    v.append(vv)
dp=[[0]*(k+1) for _ in range(n)]
for i in range(n):
    for j in range(k+1):
        if w[i]<=j:
            dp[i][j]=max(dp[i-1][j],v[i]+dp[i-1][j-w[i]])
        else:
            dp[i][j]=dp[i-1][j]
    print(dp[i])
print(dp[n-1][k])
'''

6 4 3 5
13 8 6 12



'''