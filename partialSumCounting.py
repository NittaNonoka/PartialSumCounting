import pandas as pd
n = int(input())
a_list = list(map(int, input().split()))
A =int(input())

# dp[i+1][j] : i個の中から何個か選んで総和をjにする方法が何通りあるか
# i : 0~n-1
# j : 0~A
# 漸化式
# 選んだ時　+ 選ばない時
# dp[i+1][j] = dp[i][j-a] + dp[i][j]
# j-a<0の時
# dp[i+1][j] = dp[i][j]

# 初期値　dp[0][0]=1 他は0

dp = [[0 for _ in range(A+1)] for _ in range(n+1)]
dp[0][0] = 1

for i, a in enumerate(a_list):
    for j in range(A+1):
        if j < a:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = dp[i][j] + dp[i][j-a]

print(dp[n][A])

# # dpを出力
# s = pd.DataFrame(dp, index=[0]+a_list)
# print(s)