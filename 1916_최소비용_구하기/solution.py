# 기본 다익스트라 구현 문제
# 원래는 딕셔너리 안에 딕셔너리 형식으로 그래프를 만들었었는데
# 같은 노선에서 더 작은 거리가 나오면 작은 거리로 갱신이 안되서
# 딕셔너리 안에 리스트 형식으로 바꿨다.

import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')

import heapq

def dijkstra(start, graph):
    # start로 부터 거리 무한대로 초기화
    distances = {node: float('inf') for node in graph}
    # 시작점 거리 0으로 시작
    distances[start] = 0
    queue = []
    # 시작점 큐에 대입
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # 현재거리, 현재노드
        curr_dist, curr_dest = heapq.heappop(queue)

        # 기존 거리보다 크면 볼필요가 없다.
        if distances[curr_dest] < curr_dist:
            continue
        
        for new_dest, new_dist in graph[curr_dest]:
            # 다음 노드로의 거리
            distance = curr_dist + new_dist

            # 저장되있는 거리보다 작으면 갱신
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(queue, [distances[new_dest], new_dest])
    
    return distances


N = int(input())
M = int(input())

graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    a, b, cost = map(int, input().split())
    # print(a, b, cost)
    graph[a].append((b, cost))
# print(graph)

start, end = map(int, input().split())
answer = dijkstra(start, graph)
# print(answer)

print(answer[end])

