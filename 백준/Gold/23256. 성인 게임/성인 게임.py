t=int(input())
main_dp=[0]*1000001
sub_dp=[0]*1000001
main_dp[1],main_dp[2]=7,33
sub_dp[1],sub_dp[2]=3,13
for i in range(3,1000001):
    main_dp[i]=(3*main_dp[i-1]+4*sub_dp[i-1])%1000000007
    sub_dp[i]=(main_dp[i-1]+2*sub_dp[i-1])%1000000007
for _ in range(t):
    print(main_dp[int(input())])