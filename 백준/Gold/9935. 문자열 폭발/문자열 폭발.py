from collections import deque
import sys
s=deque(list(sys.stdin.readline().strip()))
ss=list(sys.stdin.readline().strip())
ss=ss[::-1]
n=len(ss)
answer=[]
for i in range(len(s)):
    answer.append(s.pop())
    try:
        if answer[-n:]==ss:
            del answer[-n::]
    except:
        pass
if answer:
    print("".join(answer)[::-1])
else:
    print("FRULA")