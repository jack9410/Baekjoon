import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


default_ch = 100

N = input()
broken_num = int(input())
broken_num_lst = list(map(str, input().split()))
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in broken_num_lst:
    if i in num:
        num.remove(i)

print(num)

print(N, broken_num, broken_num_lst)

# 예제 1
# 5457
# 3
# 6 7 8
# 예제 2
# 100
# 5
# 0 1 2 3 4
# 예제 3
# 500000
# 8
# 0 2 3 4 6 7 8 9

