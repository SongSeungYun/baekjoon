n=int(input())
answer=1
while True:
    if n<=4:
        answer=(answer*n)%10007
        break
    answer=(answer*3)%10007
    n-=3
print(answer)