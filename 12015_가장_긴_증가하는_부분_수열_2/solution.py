# 참고: https://suri78.tistory.com/199
# LIS 를 정확하게 만드는게 아니라 길이가 같은 리스트를 만드는게 포인트
# bisect 함수 이해하기

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from bisect import bisect_left

N = input()
myArr = list(map(int, input().split()))
# print(N, myArr)

LIS = [0]

for i in myArr:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        LIS[bisect_left(LIS,i)] = i

print(len(LIS)-1)