l,c=map(int,input().split(" "))
string_list=sorted(list(input().split(" ")))

def ganeung(s):
    moem=0
    jaem=0
    for i in s:
        if i in ('a','e','i','o','u'):
            moem+=1
        else:
            jaem+=1
    return moem>0 and jaem>1

def rec(s,n):
    if len(s)==l and ganeung(s):
        print(s)
        return
    if n<len(string_list):
        rec(s+string_list[n],n+1)
        rec(s,n+1)
rec("",0)