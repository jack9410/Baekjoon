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
    # 원소가 하나라도 남아있으면 반복
    while len(left) > 0 or len(right) > 0:
        # 둘다 있을때
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 왼쪽만 있을때
        elif len(left) > 0:
            result.append(left.pop(0))
        # 오른쪽만 있을때
        elif len(right) > 0:
            result.append(right.pop(0))
    
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
