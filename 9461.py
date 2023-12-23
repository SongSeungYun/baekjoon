#dp 점화식 a n=a n-1 + a n-5 (n>=6)
t=int(input())
nums=[]
for _ in range(t):
    nums.append(int(input()))
dp=[0,1,1,1,2,2]
for num in nums:
    len_dp=len(dp)
    if len_dp>num:
        print(dp[num])
    else:
        for i in range(len_dp,num+1):
            dp.append(dp[-1]+dp[-5])
        print(dp[num])
'''
1 1 1 2 2 3 4 5 7 9 12 16
1칸뒤, 5칸뒤
'''