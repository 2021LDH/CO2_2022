def Q1(): #5972번 택배 배송
    import sys
    input = sys.stdin.readline
    from heapq import heappop,heappush #어쩔 수 없이

    def dijkstra(x):
        cost[x]= 0
        queue = []
        heappush(queue, [0, x]) #어쩔 수 없이
        #queue.append((0, x))
        while queue:
            sum, standard = heappop(queue) #어쩔 수 없이
            #sum, standard = queue[0]
            #del queue[0]
            for next, nextcost in arr[standard]:
                if cost[next] > sum + nextcost:
                    cost[next] = sum + nextcost
                    heappush(queue,[cost[next], next]) #어쩔 수 없이
                    #queue.append((cost[next], next))
        print(cost[n])

    n, m = map(int, input().split())
    arr = [[]for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
        arr[b].append((a, c))
    cost = [100000000] * (n + 1)
    dijkstra(1)
Q1()#