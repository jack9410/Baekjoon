import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

def graph_print(graph):
    for i in graph:
        print(i)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(start):
    global cnt
    stack = deque([start])
    while stack:
        # print(stack)
        curr_x, curr_y = stack.pop()
        for i in range(8):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            # 범위 확인
            if 0 <= next_x < w and 0 <= next_y < h:
                # 방문, 땅인지 확인
                if not visited[next_y][next_x] and graph[next_y][next_x] == '1':
                    visited[next_y][next_x] = True
                    stack.append((next_x, next_y))
                    
    cnt += 1


    

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        # print(w, h)
        graph = []
        visited = [[False] * w for _ in range(h)]
        for _ in range(h):
            line = input().split()
            graph.append(line)

    global cnt
    cnt = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == '1' and not visited[y][x]:
                dfs((x,y))

    print(cnt)