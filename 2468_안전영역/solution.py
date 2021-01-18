import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

from collections import deque

N = int(input())
land = [list(map(int, input().split())) for _ in range(N) ]

# print(land)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <=ny < N:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([nx, ny])
                    

tmp_lst = []

for rain in range(100):
    visited = [[False]*N for _ in range(N)]
    n = 0

    for y in range(N):
        for x in range(N):
            if land[y][x] <= rain:
                visited[y][x] = True

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                bfs(x,y)
                n += 1

    tmp_lst.append(n)

# print(tmp_lst)
print(max(tmp_lst))
