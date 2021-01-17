import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

N = int(input())
max_height = 0
land = [list(map(int, input().split())) for _ in range(N) ]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[True]*N for _ in range(N)]
print(visited)

def inBound(x,y):
    if 0<=x<N and 0<=y<N:
            return True
    else:
        return False

def find(x, y rain):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if inBound(nx, ny):
            if visited


for rain in range(100):

