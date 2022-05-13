def Q1(): #2210번 숫자판 점프
    def dfs(x, y, number):
        if len(number)==6:
            if number not in result:
                result.append(number)
            return

        movex = [1,-1,0,0]
        movey = [0,0,1,-1]
        for i in range(4):
            nextx = x + movex[i]
            nexty = y + movey[i]
            if not 0 <= nextx <= 4 or not 0 <= nexty <= 4:
                continue
            else:
                dfs(nextx, nexty, number + arr[nextx][nexty])

    arr = [[0]*5 for _ in range(5)]
    for i in range(5):
        arr[i] = list(map(str, input().split()))
    
    result = []
    for i in range(5):
        for j in range(5):
          dfs(i,j,arr[i][j])
    print(len(result))

def Q2(): #3187번 양치기 꿍
    import sys
    sys.setrecursionlimit(10 ** 6)
    
    def dfs(x, y):
        if x <= -1 or x >= row or y <= -1 or y >= column:
            return False
    
        if field[x][y] != "#":
    
            compare.append(field[x][y])
    
            field[x][y] = "#"
    
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
    
            return True
        return False
    
    row, column = map(int, sys.stdin.readline().split())
    field = [list(map(str, input())) for _ in range(row)]
    
    compare = []
    survive_wolf = []
    survive_sheep = []
    for i in range(row):
        for j in range(column):
            if field[i][j] != "#":
                dfs(i, j)
    
                if compare.count('v') < compare.count('k'):
                    survive_sheep.append(compare.count('k'))
                else:
                    survive_wolf.append(compare.count('v'))
    
                compare = []
    
    print(sum(survive_sheep), sum(survive_wolf))

def Q3(): #14248번 점프 점프
    def bfs(start):
        queue = []
        already = [0] * n
        count = 0

        queue.append(start)
        
        while queue:
            standard = queue[0]
            already[standard] = 1
            count += 1

            for i in [rock[standard], -rock[standard]]:
                if 0 <= standard + i < n and already[standard + i] == 0:
                    queue.append(standard + i)
                    already[standard + i] = 1
            del queue[0]
        return count

    n = int(input())
    rock = list(map(int, input().split()))
    start = int(input()) - 1

    count = bfs(start)
    print(count)

def Q4(): #14217번 그래프 탐색
    import sys

    def bfs(x):
        queue = []
        distance = [-1] * (n + 1)
        queue.append(x)
        distance[1] = 0

        while queue:
            standard = queue[0]
            for i in road[standard]:
                if distance[i] == -1:
                    queue.append(i)
                    distance[i] = distance[standard] + 1
            del queue[0]
        return distance

    n, m = map(int, input().split())
    road = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        road[a].append(b)
        road[b].append(a)
    q = int(input())
    revise = [[0]*3 for _ in range(q)]
    for i in range(q):
        revise[i] = list(map(int, sys.stdin.readline().split()))

    distance = bfs(1)
    for i in range(q):
        if revise[i][0] == 1:
            road[revise[i][1]].append(revise[i][2])
            road[revise[i][2]].append(revise[i][1])
        else:
            road[revise[i][1]].remove(revise[i][2])
            road[revise[i][2]].remove(revise[i][1])
        distance = bfs(1)
        for i in range(1, n + 1):
            print(distance[i] ,end=" ")
        print()
Q4()