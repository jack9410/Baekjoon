from heapq import heappop, heappush

INF = float('inf')

def dikjkstra(n, x, road):
    dist = [INF] * n
    dist[x] = 0
    q = []
    heappush(q, [0,x])

    while q:
        
        cost, pos = heappop(q)

        for curr_pos, time in road[pos]:
            time += cost
            if time < dist[curr_pos]:
                dist[curr_pos] = time
                heappush(q, [time, curr_pos])
        
    return dist
    


N, M, X = map(int, input().split())
road = [[] for _ in range(N)]

for _ in range(M):
    start, end, time = map(int, input().split())
    road[start - 1].append([end-1, time])

# print(road)

answer = [0] * N
for i in range(N):
    # print('다익스트라', i)
    dik_lst = dikjkstra(N, i, road)
    
    if i == X-1:
        for idx, r in enumerate(dik_lst):
            answer[idx] += r
    else:
        answer[i] += dik_lst[X-1]

print(max(answer))
    