import heapq
import sys

# 電報
# ダイクストラ法
INF = int(1e9)
n, m, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(d, max_distance)

print(count - 1, max_distance)
