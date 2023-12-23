import sys
def solution():
    n=int(input())
    l=[]
    for _ in range(n):
        l.append(list(map(int,sys.stdin.readline().split())))
    dp=[l[0][:]]+[[0,0,0] for _ in range(n-1)]
    for i in range(1,n):
        dp[i][0]=min(l[i][0]+dp[i-1][1],l[i][0]+dp[i-1][2])
        dp[i][1]=min(l[i][1]+dp[i-1][0],l[i][1]+dp[i-1][2])
        dp[i][2]=min(l[i][2]+dp[i-1][0],l[i][2]+dp[i-1][1])
        print(dp)
    return min(dp[-1])
print(solution())