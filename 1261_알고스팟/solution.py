# bfs로 풀었다

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

def bfs(start):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    start_y, start_x = start
    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = 0

    while queue:
        # print(queue)
        tmp_y, tmp_x = queue.popleft()
        curr_cnt = visited[tmp_y][tmp_x]
        for i in range(4):
            next_y, next_x = tmp_y + dx[i], tmp_x + dy[i]
            if 0 <= next_y < N and 0 <= next_x < M:
                if graph[next_y][next_x] == '0':
                    if visited[next_y][next_x] > curr_cnt:
                        visited[next_y][next_x] = curr_cnt
                        queue.append((next_y, next_x))
                else:
                    if visited[next_y][next_x] > curr_cnt + 1:
                        visited[next_y][next_x] = curr_cnt + 1
                        queue.append((next_y, next_x))
                        # print(queue)
                        # print(visited)
    # print(visited)
    return visited[N-1][M-1]


INF = float('inf')
M, N = map(int, input().split())

graph = []
visited = [[INF] * M for _ in range(N)]

for _ in range(N):
    graph.append(input())

# print(graph)
# print(visited)

answer = bfs((0,0))
print(answer)


