# 기본적인 다익스트라 구현 문제지만 오래걸렸다.
# 일단 방향성이 있는지 없는지 확인 제대로 하기
# 간선이 복수로 주어질때 최소값인지 확인해주고 그래프 업데이트 해주기

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        curr_dist, curr_dest = heapq.heappop(queue)
        
        # 기존에 있는 거리보다 길면 볼필요 없다
        if distances[curr_dest] < curr_dist:
            continue

        for new_dest, new_dist in graph[curr_dest].items():
            distance = new_dist + curr_dist
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(queue, [distance, new_dest])
                # print(distances)
        
    return distances
        

V, E = map(int, input().split())
# print(V, E)
K = int(input())

graph = {}

for i in range(1, V+1):
    graph[i] = {}

for _ in range(E):
    u, v, w = map(int, input().split())
    # 그래프에 바로 넣으면 안되고 최소값인지 확인하고 넣어줘야한다.
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
        else:
            continue
    else:
        graph[u][v] = w

# print(graph)

answer = dijkstra(graph, K)
# print(answer)

for i in answer.values():
    if i == float('inf'):
        print('INF')
    else:
        print(i)


