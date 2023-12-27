import sys
a=sys.stdin.readline().strip()
b=sys.stdin.readline().strip()
len_a=len(a)
len_b=len(b)
dp=[0]*len_b
for i in range(len_a):
    num=0
    for j in range(len_b):
        if num<dp[j]:
            num=dp[j]
        elif a[i]==b[j]:
            dp[j]=num+1
print(max(dp))
'''
ACAYKP
CAPCAK

OOOOXXXXXF
OOXFXXXQf



ABCDEXXXXXF
ABCDEXFXXXQ

000000
101110
102220
102330
102340
102340
122340

'''