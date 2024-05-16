t=int(input())
divisors=[25,10,5,1]
for _ in range(t):
    c=int(input())
    answer=""
    for d in divisors:
        answer+=str(c//d)+" "
        c%=d
    print(answer)