def sol(n,m,crain,box):
    if crain[0]<box[0]:
        return -1
    box_on_crain=[0]*n
    for cur_box_index in range(m):
        min_crain_index=0
        for cur_crain_index in range(1,n):
            if box[cur_box_index]>crain[cur_crain_index]:
                break
            if box_on_crain[min_crain_index]>box_on_crain[cur_crain_index]:
                min_crain_index=cur_crain_index
        box_on_crain[min_crain_index]+=1
    return max(box_on_crain)

n=int(input())
crain=sorted(list(map(int,input().split(" "))),reverse=True)
m=int(input())
box=sorted(list(map(int,input().split(" "))),reverse=True)
# print(crain)
# print(box)
# print()
print(sol(n,m,crain,box))