from collections import deque
n=int(input())
l=deque(map(int,input().split(" ")))
ballons=deque([i for i in range(1,n+1)])
answer=""
dx=1
for j in range(n):
    len_list=n-j+1
    dx=dx//(n-j)
    print()
    #최단경로로 풍선을 터치기 위한 loc값 설정
    if dx>=0 and abs(dx)<=abs(len_list-abs(dx)):
        loc=dx
    elif dx>=0 and abs(dx)>abs(len_list-abs(dx)):
        loc=abs(dx)-len_list
    elif dx<0 and abs(dx)<=abs(len_list-abs(dx)):
        loc=dx
    elif dx<0 and abs(dx)>abs(len_list-abs(dx)):
        loc=len_list-abs(dx)
    #이동하고 풍선 터치기
    if loc>0:
        for i in range(loc-1):
            ballons.append(ballons.popleft())
            l.append(l.popleft())
        answer+=str(ballons.popleft())+" "
        dx=l.popleft()
    else:
        for i in range(abs(loc)-1):
            ballons.appendleft(ballons.pop())
            l.appendleft(l.pop())
        answer+=str(ballons.pop())+" "
        dx=l.pop()
print(answer)

'''
1 2 3 4 5
3 2 1 -3 -1

1 2 3 4 5
1

2 3 4 5
-2
5 2 3 4

5 2 3
1

'''