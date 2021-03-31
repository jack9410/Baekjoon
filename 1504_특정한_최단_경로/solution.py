# 다익스트라 기본 구현
# 마지막 무제한 거리 출력 처리 때문에 틀렸다.

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

import heapq
INF = float('inf')

def dijkstra(start, graph):
    distances = {node:INF for node in graph}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        curr_dist, curr_dest = heapq.heappop(queue)

        if curr_dist > distances[curr_dest]:
            continue
        for new_dest, new_dist in graph[curr_dest]:
            distance = curr_dist + new_dist
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(queue, [distance, new_dest])
    
    return distances



N, E = map(int, input().split())

graph = {}
for i in range(1, N+1):
    graph[i] = []


for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = dijkstra(1, graph)
dist2 = dijkstra(v1, graph)
dist3 = dijkstra(v2, graph)
# print(dist1, dist2, dist3)

answer1 = dist1[v1] + dist2[v2] + dist3[N]
answer2 = dist1[v2] + dist3[v1] + dist2[N]

answer = min(answer1, answer2)

if answer < INF:
    print(answer)
else:
    print(-1)

