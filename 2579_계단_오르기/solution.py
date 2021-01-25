# 틀림
# 1 일때 생각하자

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())
arr = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(N):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0]+ arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

# print(dp)
print(dp[N-1])



