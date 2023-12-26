#11054 가장 긴 바이토닉 부분 수열 // 11053이랑 같은 케이스

import sys
n=int(input())
l=list(map(int,sys.stdin.readline().split()))

dp_incre=[[1,l[0]]]+[[0,0] for _ in range(n-1)]
for i in range(1,n):
    max_num=0
    for j in range(i-1,-1,-1):
        if l[j]<l[i]:
            max_num=max(dp_incre[j][0],max_num)
    dp_incre[i]=[max_num+1,l[i]]

l=l[::-1]
dp_decre=[[1,l[0]]]+[[0,0] for _ in range(n-1)]
for i in range(1,n):
    max_num=0
    for j in range(i-1,-1,-1):
        if l[j]<l[i]:
            max_num=max(dp_decre[j][0],max_num)
    dp_decre[i]=[max_num+1,l[i]]
dp_decre.reverse()

answer=[]
for i in range(n):
    answer.append(dp_incre[i][0]+dp_decre[i][0])
print(max(answer)-1)