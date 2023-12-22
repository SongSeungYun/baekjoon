from collections import deque
n=int(input())
l=deque(map(int,input().split(" ")))
q=deque((dx,i+1) for i,dx in enumerate(l))
answer=""
for pop_num in range(1,n):
    dx,i=q.popleft()
    answer+=str(i)+" "
    if dx>=0:
        q.rotate(1-dx)
    else:
        q.rotate(-dx)
print(answer+str(q.pop()[1]))