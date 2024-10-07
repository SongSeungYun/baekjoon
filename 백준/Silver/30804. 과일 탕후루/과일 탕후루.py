import sys
input=sys.stdin.readline
n=int(input())
tanghuru=list(map(int,input().split(" ")))
fruits=[0]*9
a,b=0,0
now_len=0
answer=0
if_break=False
while True:
    while (fruits.count(0)>7 or
           fruits.count(0)==7 and fruits[tanghuru[b]-1]!=0):
        b+=1
        now_len+=1
        if b==n:
            answer=max(answer,now_len)
            if_break=True
            break
        fruits[tanghuru[b-1]-1]+=1
        answer=max(answer,now_len)
    if if_break:
        break
    a+=1
    now_len-=1
    fruits[tanghuru[a-1]-1]-=1
print(answer)