#2156 포도주 시식 dp //
def solution():
    n=int(input())
    wines=[]
    for _ in range(n):
        wines.append(int(input()))
    if n==1:
        return wines[0]
    elif n==2:
        return wines[0]+wines[1]
    elif n==3:
        return max(wines[0]+wines[1],wines[1]+wines[2],wines[0]+wines[2])
    dp=[0]*n
    dp[0]=wines[0]
    dp[1]=wines[0]+wines[1]
    dp[2]=wines[0]+wines[2]
    for i in range(3,n):
        dp[i]=max(wines[i]+dp[i-2],wines[i]+wines[i-1]+dp[i-3])
    return max(dp[-1],dp[-2])
print(solution())
'''



'''