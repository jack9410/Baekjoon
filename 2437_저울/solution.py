import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())
weight = list(map(int, input().split()))

weight.sort()
# print(N, weight)

tmp_sum = 0

for i in range(N):
    if tmp_sum + 1 >= weight[i]:
        tmp_sum += weight[i]
    else:
        break

print(tmp_sum + 1)