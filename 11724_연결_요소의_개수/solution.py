# 연결요소 (Connected Component) 가 무엇인지 몰랐다.
# 기본 dfs 구현

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

def dfs(start):
    conn_comp = []
    stack = deque([start])

    while stack:
        # print(stack)
        curr = stack.pop()
        if not curr in visited:
            visited.append(curr)
            conn_comp.append(curr)
            stack.extend(graph[curr])
    return conn_comp


N, M = map(int, input().split())

graph = {}
visited = []
cnt = 0

for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    tmp = dfs(i)
    # print(tmp)
    if tmp:
        cnt += 1

print(cnt)