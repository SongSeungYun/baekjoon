import sys
import heapq
input=lambda:sys.stdin.readline().strip()
n=int(input())
front=[(10001,-10001)]#최대힙
back=[10001]#최소힙
mid=int(input())#중간값
print(mid)
for i in range(n-1):
    cur=int(input())
    #print(sorted(front),mid,sorted(back))
    if i%2==0:#입력받기 전 총 숫자가 홀수
        if cur>=mid:
            heapq.heappush(back,cur)
        elif front[0][1]<=cur<mid:
            heapq.heappush(back,mid)
            mid=cur
        else:
            heapq.heappush(back,mid)
            mid=heapq.heappop(front)[1]
            heapq.heappush(front,(-cur,cur))
    else:#입력받기 전 총 숫자가 짝수
        if cur>=back[0]:
            heapq.heappush(front,(-mid,mid))
            mid=heapq.heappop(back)
            heapq.heappush(back,cur)
        elif mid<=cur<back[0]:
            heapq.heappush(front,(-mid,mid))
            mid=cur
        else:
            heapq.heappush(front,(-cur,cur))
    print(mid)
    #print("미드:",mid)