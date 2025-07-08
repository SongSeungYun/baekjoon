import sys
input=lambda:sys.stdin.readline().strip()
munjang=input()
m=len(munjang)
n=int(input())
words=[]
for _ in range(n):
    words.append(input())

def cal_cost(a,b):
    if sorted(list(a))!=sorted(list(b)):
        return -1
    # result=0
    return len(a)-sum((a[i]==b[i]) for i in range(len(a)))
    # for i in range(len(a)):
    #     result+=a[i]==b[i]
    # return result
    

dp=[[-1]*(m+1) for _ in range(n+1)]
for i in range(m+1):
    dp[0][i]=0
for i in range(n+1):
    dp[i][0]=0
for i in range(1,m+1):
    for j in range(1,n+1):
        word_len=len(words[j-1])
        if i>=word_len:
            cal_result=cal_cost(munjang[i-word_len:i],words[j-1])
            if cal_result==-1:
                continue
            min_=51
            for k in range(1,n+1):
                if dp[k][i-word_len]!=-1:
                    min_=min(min_,dp[k][i-word_len])
            if min_!=51:
                dp[j][i]=min_+cal_result
            #print(i,j,i-word_len,min_)
# for i in dp:
#     print(i)

answer=51
for i in range(1,n+1):
    if dp[i][m]!=-1:
        answer=min(answer,dp[i][m])
if answer==51:
    print(-1)
else:
    print(answer)