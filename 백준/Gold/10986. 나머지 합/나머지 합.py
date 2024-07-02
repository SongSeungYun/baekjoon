import sys
n,m=map(int,input().split(" "))
l=list(map(int,sys.stdin.readline().strip().split(" ")))
fibo=[0]
for i in range(1,n+1):
    fibo.append(fibo[-1]+i)
maps=[0]
for i in l:
    maps.append(maps[-1]+i)
answer=0
d={i:0 for i in range(m)}
for i in range(n+1):
    d[maps[i]%m]+=1
for i in range(m):
    if d[i]!=0 and d[i]!=1:
        answer+=fibo[d[i]-1]
print(answer)