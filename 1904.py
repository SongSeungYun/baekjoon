#간단한 dp 점화식 문제, 피보나치
n=int(input())
l=[0,1,2]
for i in range(n-2):
    l.append((l[-1]+l[-2])%15746)
print(l[n])

'''
1 1
2 2
3 3
4 5
'''