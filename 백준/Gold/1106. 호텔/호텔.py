import sys
input=sys.stdin.readline

c,n=map(int,input().split(" "))
cities=[]
for _ in range(n):
    cities.append(tuple(map(int,input().split(" "))))

dp=[[0]*1001 for _ in range(n)]

cost,population=cities[0]
for i in range(1,1001):
    dp[0][i]=((i-1)//population+1)*cost

for j in range(1,n):
    cost,population=cities[j]
    for i in range(1,population):
        dp[j][i]=min(((i-1)//population+1)*cost,dp[j-1][i])
    for i in range(population,1001):
        dp[j][i]=min(dp[j][i-population]+cost,dp[j-1][i])
print(dp[n-1][c])