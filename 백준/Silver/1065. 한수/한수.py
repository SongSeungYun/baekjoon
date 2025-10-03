def if_hansu(n):
    if n<10:
        return True
    str_n=str(n)
    gongcha=int(str_n[0])-int(str_n[1])
    for i in range(1,len(str_n)-1):
        if int(str_n[i])-int(str_n[i+1])!=gongcha:
            return False
    return True

n=int(input())
answer=0
for i in range(1,n+1):
    answer+=int(if_hansu(i))
print(answer)