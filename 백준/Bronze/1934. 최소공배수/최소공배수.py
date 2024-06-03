def aaa(a,b):
    n=min(a,b)
    for i in range(n,0,-1):
        if a%i==0 and b%i==0:
            return a*b//i
t=int(input())
for _ in range(t):
    a,b=map(int,input().split(" "))
    print(aaa(a,b))