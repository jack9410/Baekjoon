import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '/input.txt', 'r')

from collections import deque

def graph_print(graph):
    for i in graph:
        print(i)
dx = [0,0,1,-1]
dy = [1,-1,0,0]


M, N = map(int, input().split())
# print(M, N)

graph = []
visited = [[False]*M for _ in range(N)]
for _ in range(N):
    line = input().split()
    graph.append(line)
# graph_print(graph)
# graph_print(visited)

q = deque()

for y in range(N):
    for x in range(M):
        if graph[y][x] == '1':
            q.append((y,x))
            visited[y][x] = True
        elif graph[y][x] == '-1':
            visited[y][x] = True

# print(q)

def bfs(queue):
    next_queue = deque()
    for i in queue:
        curr_y, curr_x = i
        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if not visited[next_y][next_x] and graph[next_y][next_x] == '0':
                    graph[next_y][next_x] = '1'
                    visited[next_y][next_x] = True
                    next_queue.append((next_y, next_x))
    # print(next_queue)
    return next_queue

cnt = -1
while q:
    q = bfs(q)
    cnt += 1


for i in graph:
    if '0' in i:
        print(-1)
        exit(0)

print(cnt)


