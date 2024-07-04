def calculate(a,b,bb):
    if bb=="+":
        return a+b
    elif bb=="-":
        return a-b
    elif bb=="*":
        return a*b
    elif bb=="/":
        if a<0:
            return (-1)*(abs(a)//b)
        else:
            return a//b
    
def back(num,b,l):
    global min_answer
    global max_answer
    if l==n-1:
        min_answer=min(num,min_answer)
        max_answer=max(num,max_answer)
    for i in range(4):
        if b[i]>0:
            b[i]-=1
            back(calculate(num,nums[l+1],buho[i]),b,l+1)
            b[i]+=1

n=int(input())
nums=list(map(int,input().split(" ")))
buho=["+","-","*","/"]
buho_num=list(map(int,input().split(" ")))
min_answer=10**9+1
max_answer=-10**9-1
back(nums[0],buho_num,0)
print(int(max_answer))
print(int(min_answer))