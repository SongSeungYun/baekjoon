import sys
import heapq
input=sys.stdin.readline
heap=[]
n=int(input())
for _ in range(n):
    temp=int(input())
    if temp:
        heapq.heappush(heap, -1*temp)
    else:
        if heap:
            print(-1*heapq.heappop(heap))
        else:
            print(0)