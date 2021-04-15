# 버블소트 구현
# 시간 복잡도 O(n^2)
# 장점: 구현이 쉽다, 직관적이다
# 단점: 최선이든 최악이든 O(n^2), 원소의 개수가 많아질수록 성능 저하

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())

my_lst = []

for _ in range(N):
    my_lst.append(int(input()))

# print(my_lst)

for idx in range(N-1, -1, -1):
    # print(idx)
    for j in range(idx):
        if my_lst[j] > my_lst[j+1]:
            tmp = my_lst[j]
            my_lst[j] = my_lst[j+1]
            my_lst[j+1] = tmp

for i in my_lst:
    print(i)

        