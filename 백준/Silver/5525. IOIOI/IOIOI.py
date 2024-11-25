n=int(input())
m=int(input())
s=input()
i,answer,ioi=0,0,0
while i<m-1:
    if s[i:i+3]=="IOI":
        i+=2
        ioi+=1
        if ioi>=n:
            answer+=1
    else:
        i+=1
        ioi=0
print(answer)