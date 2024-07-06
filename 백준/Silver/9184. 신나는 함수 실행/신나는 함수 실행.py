import time
dp=[[[0]*21 for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        dp[i][j][0]=1
        dp[i][0][j]=1
        dp[0][i][j]=1

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i<j<k:
                dp[i][j][k]=dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
            else:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1]

while True:
    my_input=input()
    if my_input=="-1 -1 -1":
        break
    a,b,c=map(int,my_input.split(" "))
    answer=0
    if a<=0 or b<=0 or c<=0:
        answer=1
    elif a>20 or b>20 or c>20:
        answer=dp[20][20][20]
    else:
        answer=dp[a][b][c]
    print("w(",a,", ",b,", ",c,") = ",answer,sep="")