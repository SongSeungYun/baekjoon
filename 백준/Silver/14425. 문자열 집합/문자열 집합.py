n,m=list(map(int,input().split(" ")))
s1=set()
answer=0
for _ in range(n):
    s1.add(input())
for _ in range(m):
    answer+=int(input() in s1)
print(answer)