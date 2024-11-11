n,m=map(int,input().split(" "))
mapp=[list(map(int,input().split(" "))) for i in range(n)]
def blue():
    answer=0
    ####
    for i in range(n):
        for j in range(m-3):
            answer=max(answer,mapp[i][j]+mapp[i][j+1]+mapp[i][j+2]+mapp[i][j+3])
    #
    #
    #
    #
    for i in range(n-3):
        for j in range(m):
            answer=max(answer,mapp[i][j]+mapp[i+1][j]+mapp[i+2][j]+mapp[i+3][j])
    return answer
def yellow():
    answer=0
    ##
    ##
    for i in range(n-1):
        for j in range(m-1):
            answer=max(answer,mapp[i][j]+mapp[i+1][j]+mapp[i][j+1]+mapp[i+1][j+1])
    return answer
def orange():
    answer=0
    #
    #
    ##
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j]+mapp[i+1][j]+mapp[i+2][j]+mapp[i+2][j+1])
     #
     #
    ##
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j+1]+mapp[i+1][j+1]+mapp[i+2][j]+mapp[i+2][j+1])
    ###
    #
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j]+mapp[i][j+1]+mapp[i][j+2]+mapp[i+1][j])
    ###
      #
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j]+mapp[i][j+1]+mapp[i][j+2]+mapp[i+1][j+2])
    ##
     #
     #
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j]+mapp[i][j+1]+mapp[i+1][j+1]+mapp[i+2][j+1]) 
    ##
    #
    #
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j]+mapp[i][j+1]+mapp[i+1][j]+mapp[i+2][j]) 
      #
    ###
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j+2]+mapp[i+1][j]+mapp[i+1][j+1]+mapp[i+1][j+2])
    #
    ###
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j]+mapp[i+1][j]+mapp[i+1][j+1]+mapp[i+1][j+2])
    return answer
def green():
    answer=0
    
    #
    ##
     #
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j]+mapp[i+1][j]+mapp[i+1][j+1]+mapp[i+2][j+1]) 
     ##
    ##
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j+1]+mapp[i][j+2]+mapp[i+1][j]+mapp[i+1][j+1])
     #
    ##
    #
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j+1]+mapp[i+1][j]+mapp[i+1][j+1]+mapp[i+2][j]) 
    ##
     ##
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j]+mapp[i][j+1]+mapp[i+1][j+1]+mapp[i+1][j+2])
    return answer
def pink():
    answer=0
    
     #
    ###
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j+1]+mapp[i+1][j]+mapp[i+1][j+1]+mapp[i+1][j+2])
    #
    ##
    #
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j]+mapp[i+1][j]+mapp[i+1][j+1]+mapp[i+2][j])
     #
    ##
     #
    for i in range(n-2):
        for j in range(m-1):
            answer=max(answer,mapp[i][j+1]+mapp[i+1][j]+mapp[i+1][j+1]+mapp[i+2][j+1])
    ###
     #
    for i in range(n-1):
        for j in range(m-2):
            answer=max(answer,mapp[i][j]+mapp[i][j+1]+mapp[i][j+2]+mapp[i+1][j+1])
    return answer
     
print(max(blue(),yellow(),orange(),green(),pink()))