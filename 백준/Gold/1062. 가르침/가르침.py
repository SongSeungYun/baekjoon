n,k=map(int,input().split(" "))
words=[]
for i in range(n):
    words.append(input())
if k<5:
    print(0)
    exit()
d=[0]*26
acint=[0,2,8,13,19]
for i in acint:
    d[i]=1
answer=0
def dfs(index,cnt):
    global answer
    if cnt==k-5:
        readcnt=0
        for word in words:
            if_can_read=True
            for alpha in word:
                if not d[ord(alpha)-97]:
                    if_can_read=False
                    break
            if if_can_read:
                readcnt+=1
        answer=max(answer,readcnt)
        return
    for i in range(index,26):
        if not d[i]:
            d[i]=1
            dfs(i,cnt+1)
            d[i]=0
dfs(0,0)
print(answer)