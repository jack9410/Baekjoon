# 오답

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

def arr_print(array):
    for i in array:
        print(i)

def min_row_sum(array):
    row_sum = []
    for i in array:
        row_sum.append(sum(i))
    print(min(row_sum), end='')

def rotate(r, c, s, array):
    r = r-1
    c = c-1
    new_array = [[0] * M for _ in range(N)]

    for i in range(1, s+1):
        # 윗 열
        new_array[r-i][c-i+1 : (c+i)+1] = array[r-i][c-i : (c+i-1) + 1]
        # 밑 열
        new_array[r+i][c-i : (c+i-1) + 1] = array[r+i][c-i+1 : (c+i)+1]


    for i in range(1, s+1):
        for j in range(i*2):
            # 오른쪽 행
            new_array[(r-i+j) + 1][c+i] = array[r-i+j][c+i]
            # 왼쪽행
            new_array[r-i+j][c-i] = array[(r-i+j) + 1][c-i]

    for i in range(N):
        for j in range(M):
            if new_array[i][j] == 0:
                new_array[i][j] = array[i][j]

    # arr_print(new_array)
    # print()
    return new_array


N, M, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

next_arr = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        next_arr[i][j] = array[i][j]
# arr_print(array)
# print()



for _ in range(K):
    r, c, s = map(int, input().split())
    next_arr = rotate(r, c, s, next_arr)

min_row_sum(next_arr)

