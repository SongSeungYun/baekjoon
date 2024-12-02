import heapq
minus_heap,plus_heap=[],[]
n=int(input())
for _ in range(n):
    a=int(input())
    if a<0:
        heapq.heappush(minus_heap,-a)
    elif a>0:
        heapq.heappush(plus_heap,a)
    else:
        if not minus_heap and not plus_heap:
            print(0)
        elif not minus_heap and plus_heap:
            print(heapq.heappop(plus_heap))
        elif minus_heap and not plus_heap:
            print(-heapq.heappop(minus_heap))
        else:
            if minus_heap[0]>plus_heap[0]:
                print(heapq.heappop(plus_heap))
            else:
                print(-heapq.heappop(minus_heap))