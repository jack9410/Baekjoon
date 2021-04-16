# merge sort 구현
# 리스트 슬라이싱, list pop 사용했을떄 시간 초과 났다.

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


N = int(input())

my_lst = []

for _ in range(N):
    my_lst.append(int(input()))

# print(my_lst)

def merge(left, right):
    result = []
    i, j = 0, 0
    # 원소가 하나라도 남아있으면 반복
    while len(left) > i or len(right) > j:
        # 둘다 있을때
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # 왼쪽만 있을때
        elif len(left) > i:
            result.append(left[i])
            i += 1
        # 오른쪽만 있을때
        elif len(right) > j:
            result.append(right[j])
            j += 1
    
    return result
        

def merge_sort(my_lst):
    n = len(my_lst)
    center = n//2
    if n == 1:
        return my_lst
    else:
        left = my_lst[:center]
        right = my_lst[center:]
        return merge(merge_sort(left), merge_sort(right))

sorted_lst = merge_sort(my_lst)

for i in sorted_lst:
    print(i)
