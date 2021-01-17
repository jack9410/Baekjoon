import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N ,M = map(int, input().split())
print(N,M)

my_list = []

for i in range(N):
    my_list.append(int(input()))

print(my_list)