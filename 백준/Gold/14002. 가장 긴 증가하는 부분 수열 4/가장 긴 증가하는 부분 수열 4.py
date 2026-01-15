n=int(input())
nums=[1001]+list(map(int,input().split(" ")))
num_dp=[0]*(n+1)
index_dp={i:[] for i in range(n+1)}
num_dp[1]=1
index_dp[1]=[1]
for i in range(2,n+1):
    max_index=0
    for j in range(1,i):
        if nums[j]<nums[i] and num_dp[j]>=num_dp[max_index]:
            max_index=j
    num_dp[i]=num_dp[max_index]+1
    index_dp[i]=index_dp[max_index]+[i]
# print(num_dp)
# print(index_dp)
max_index=num_dp.index(max(num_dp))
print(num_dp[max_index])
for i in index_dp[max_index]:
    print(nums[i],end=" ")