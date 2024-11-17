t=int(input())
for _ in range(t):
    n=int(input())
    ot={}
    answer=1
    for __ in range(n):
        a,b=input().split(" ")
        if b in ot:
            ot[b]+=1
        else:
            ot[b]=1
    for value in ot.values():
        answer*=value+1
    print(answer-1)