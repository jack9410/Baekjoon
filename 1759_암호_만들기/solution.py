import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from itertools import combinations

L, C = map(int, input().split())
alphabet = input().split()
alphabet.sort()

word_lst = list(combinations(alphabet,L))


for i in word_lst:
    v = 0
    c = 0
    for j in i:
        if j in 'aeiou':
            v += 1
        else:
            c += 1

    if v >=1 and c >= 2:
        print(''.join(i))