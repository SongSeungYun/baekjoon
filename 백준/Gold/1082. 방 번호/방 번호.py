n=int(input())
p=list(map(int,input().split(" ")))
m=int(input())
dp=[[-1]*(m+1) for _ in range(n+1)]

def make_num(i,raw_num):
    if raw_num==-1:
        return i
    else:
        return int("".join(sorted(list(str(raw_num))+[str(i)],reverse=True)))

for i in range(1,n+1):
    for j in range(1,m+1):
        max_=max(dp[i-1][j],dp[i][j-1])
        for k in range(i):
            if j-p[k]>=0:
                # print(k,dp[i][j-p[k]],make_num(k,dp[i][j-p[k]]))
                max_=max(max_,make_num(k,dp[i][j-p[k]]))
        dp[i][j]=max_
        # if j>=p[i-1]:
        #     dp[i][j]=max(dp[i-1][j],dp[i][j-1],make_num(i-1,dp[i][j-p[i-1]]))
        # else:
        #     dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#     print(dp[i])
# for i in dp:
#     print(i)
print(dp[n][m])