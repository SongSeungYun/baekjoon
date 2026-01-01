def sol(s):
    if len(s)==1:
        return int(s!="0")
    
    l=[0]*len(s)
    l[0]=1

    if s[0]=="0" or s[0]>"2" and s[1]=="0":
        return 0
    if "11"<=s[:2]<="26" and s[:2]!="20":
        l[1]=2
    else:
        l[1]=1

    for i in range(2,len(s)):
        #print(i)
        if s[i]=="0" and not 0<int(s[i-1:i+1])<27:
            return 0
        #print(i,(1 if s[i]!="0" else 0),(1 if 0<int(s[i-1:i+1])<27 else 0))
        l[i]+=((l[i-1] if s[i]!="0" else 0)+(l[i-2] if 9<int(s[i-1:i+1])<27 else 0))%1000000
        #print(i,l[i])
        # l[i]+=(l[i-2]+(1 if 0<int(s[i-1:i+1])<27 else 0))%1000000
        #print("l[",i,"] : ",l[i],sep="")
    #print(l)
    return l[-1]

s=input().strip()
print(sol(s))