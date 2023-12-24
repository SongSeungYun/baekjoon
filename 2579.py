def solution():
    n=int(input())
    stairs=[]
    for _ in range(n):
        stairs.append(int(input()))
    if n==1:
        return stairs[0]
    elif n==2:
        return stairs[0]+stairs[1]
    elif n==3:
        return stairs[0]+stairs[2]
    dp=[0]*n
    dp[n-1]=stairs[n-1]
    dp[n-2]=stairs[n-1]+stairs[n-2]
    dp[n-3]=max(stairs[n-1]+stairs[n-3],stairs[n-1]+stairs[n-2])
    
    for i in range(n-4,-1,-1):
        dp[i]=max(stairs[i]+stairs[i+1]+dp[i+3],stairs[i]+dp[i+2])
    return max(dp[0],dp[1])
    

print(solution())