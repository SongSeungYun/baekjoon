import sys
n=int(input())
l=list(map(int,sys.stdin.readline().split()))
dp=[[1,l[0]]]+[[0,0] for _ in range(n)]
for i in range(1,n):
    max_num=0
    for j in range(i-1,-1,-1):
        if l[j]<l[i]:
            max_num=max(dp[j][0],max_num)
    dp[i]=[max_num+1,l[i]]
print(dp)
print(max([dp[i][0] for i in range(n)]))
'''
1.아예 처음인경우
2.직전거랑 이어지는경우
3.전에있던거랑 이어지는경우


11
100 1 2 3 101 4 5 6 102 7 8
answer 8

5
1 2 3 4 3
answer 4

2
1 1
answer 1

4
1 4 2 3
answer 3

7
70 30 50 60 70 0 10
answer 4

8
10 50 60 70 20 30 40 50
answer 5

9
5 10 50 60 70 20 30 40 50
answer 6

20
322 831 212 232 545 698 260 265 324 215 701 75 156 605 851 993 425 887 691 593
answer 8

[1,322] [2,831] [1,212] 

91 92 93  94 95 96

'''