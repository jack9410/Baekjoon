import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())

my_lst = []

for _ in range(N):
    my_lst.append(int(input()))

print(my_lst)

for idx in range(N-1, -1, -1):
    # print(idx)
    for j in range(idx):
        if my_lst[j] > my_lst[j+1]:
            tmp = my_lst[j]
            my_lst[j] = my_lst[j+1]
            my_lst[j+1] = tmp

print(my_lst)

        