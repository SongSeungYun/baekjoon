#2465 전깃줄 // 가장긴증가하는부분수열 활용한 문제, 해설보고 이해함
n=int(input())
lines=[]
for _ in range(n):
    lines.append(list(map(int,input().split())))
lines.sort()
dp=[1]*n
for i in range(n):
    for j in range(i):
        if lines[j][1]<lines[i][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))
'''
[0,1,1,2,2]
[[1, 8], [2, 2], [3, 9], [4, 1], [6, 4], [7, 6], [9, 7], [10, 10]]
8 2 9 1 4 6 7 10


1 3
3 1
2 5
4 6
6 4

3 1 5 6 4

정답 2
'''