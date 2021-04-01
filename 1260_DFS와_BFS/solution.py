# dfs bfs 어떻게 구현하는지 까먹었다 ㅜ

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

def dfs(start):
    answer = []
    visited = [False] * (N+1)
    stack = deque([start])

    while stack:
        curr_dest = stack.pop()
        if not visited[curr_dest]:
            visited[curr_dest] = True
            answer.append(curr_dest)
            # 작은 노드부터 방문해야하기 때문에 스택을 거꾸로 넣어준다
            stack.extend(sorted(graph[curr_dest], reverse=True))
    return answer

def bfs(start):
    answer = []
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque([start])

    while queue:
        curr_dest = queue.popleft()
        answer.append(curr_dest)
        # 작은 노드부터 방문해야되서 정리해서 방문한다.
        for i in sorted(graph[curr_dest]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return(answer)

N, M, V = map(int, input().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
# print(graph)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)

answer1 = dfs(V)
answer2 = bfs(V)
print(" ".join(map(str, answer1)))
print(" ".join(map(str, answer2)))