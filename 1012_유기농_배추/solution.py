# 기본적인 완전탐색 문제
# visited를 처리 잘못해줬다가 시간을 많이 날렸다.
# 연습이 더 필요함

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def print_map(graph):
    for i in graph:
        print(i)

def bfs(start):
    queue = deque([start])
    while queue:
        curr_y, curr_x = queue.popleft()
        if not visited[curr_y][curr_x]:
            visited[curr_y][curr_x] = True
            for i in range(4):
                next_y, next_x = curr_y + dy[i], curr_x + dx[i]
                if 0 <= next_y < N and 0 <= next_x < M:
                    if not visited[next_y][next_x] and matrix[next_y][next_x] == 1:
                        queue.append((next_y, next_x))
                        # 여기서 visited를 같이 처리해버려서 틀렸다.
                        # 큐에만 추가하고 직접 방문했을 때 visited 처리해주자

T = int(input())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1 and not visited[y][x]:
                bfs((y, x))
                cnt += 1
    
    print(cnt)
    