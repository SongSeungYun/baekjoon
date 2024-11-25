import sys
input=sys.stdin.readline
n,m=map(int,input().split(" "))
d={}
answer=0
db=[]
for _ in range(n):
    d[input().rstrip()]=True
for _ in range(m):
    temp=input().rstrip()
    if temp in d:
        db.append(temp)
        answer+=1

print(answer)
for i in sorted(db):
    print(i)