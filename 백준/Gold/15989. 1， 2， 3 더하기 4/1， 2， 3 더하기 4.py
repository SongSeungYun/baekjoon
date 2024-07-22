t=int(input())
dp=[0,1,2,3,4,5,7]
for i in range(7,10001):
    dp.append(dp[i-1]+dp[i-2]-dp[i-3]+1-int(bool(i%3)))
for _ in range(t):
    print(dp[int(input())])