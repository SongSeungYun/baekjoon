def rec(n,a,b):#n개의 원판을 a에서 b로 옮김
    if n==1:
        print(a,b)
        return
    rec(n-1,a,6-a-b)
    print(a,b)
    rec(n-1,6-a-b,b)
nn=int(input())
print(2**nn-1)
rec(nn,1,3)