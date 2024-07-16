n=int(input())
if n%2==1:
    print(0)
else:
    dp=[1,3]
    for i in range(n//2-1):
        dp.append(dp[-1]*4-dp[-2])
    print(dp[-1])