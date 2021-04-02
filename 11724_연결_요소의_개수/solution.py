import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

def dfs(start):
    visited = []
    


N, M = map(int, input().split())

graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)

for i in range(1, N+1):
    dfs(i)
