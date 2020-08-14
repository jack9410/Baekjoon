import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

def pushable(ch):
    for i in str(ch):
        if int(i) not in num:
            return False
    return True

default_ch = 100
num = [i for i in range(10)]

N = int(input())
# print(N)
broken_num = int(input())
if broken_num != 0:
    broken_num_lst = list(map(int, input().split()))
    for i in broken_num_lst:
        if i in num:
            num.remove(i)

if broken_num < 10:
    diff = 0
    while True:
        tmp_ch = N - diff
        # print(tmp_ch)
        if tmp_ch >= 0 and pushable(tmp_ch) :
            closest_ch = tmp_ch
            break
        tmp_ch = N + diff
        # print(tmp_ch)
        if pushable(tmp_ch):
            closest_ch = tmp_ch
            break
        diff += 1
        # print(diff)

    ans1 = len(str(closest_ch)) + abs(N - closest_ch)
    ans2 = abs(N - 100)
    print(min(ans1, ans2))
else:
    print(abs(N - 100))


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

