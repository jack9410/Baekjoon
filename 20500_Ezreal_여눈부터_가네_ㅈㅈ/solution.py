import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input)

answer = 0

dp = []

# N = 1
dp.append(0)

# N = 2
# 15, 51
dp.append(1)

# N = 3
# 111, 115, 151, 155, 511, 515, 551, 555
dp.append(1)