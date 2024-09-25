import sys
input=sys.stdin.readline
import heapq
heap=[]
n=int(input())
for _ in range(n):
    c=int(input())
    if c==0 and heap:
        print(heapq.heappop(heap))
    elif c==0 and not heap:
        print(0)
    else:
        heapq.heappush(heap,c)