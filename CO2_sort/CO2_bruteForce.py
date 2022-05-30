def Q1(): #2798번 블랙잭
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    result = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if cards[i] + cards[j] + cards[k] <= m and cards[i] + cards[j] + cards[k] > result:
                    result = cards[i] + cards[j] + cards[k]
    print(result)

def Q2(): #2231번 분해합
    n = int(input())
    for i7 in range(0, 10):
        for i6 in range(0, 10):
            for i5 in range(0, 10):
                for i4 in range(0, 10):
                    for i3 in range(0, 10):
                        for i2 in range(0, 10):
                            for i1 in range(0, 10):
                                a = 1000001 * i7 + 100001 * i6 + 10001 * i5 + 1001 * i4 + 101 * i3 + 11 * i2 + 2 * i1
                                if a == n:
                                    print(1000000 * i7 + 100000 * i6 + 10000 * i5 + 1000 * i4 + 100 * i3 + 10 * i2 + i1)
                                    return 0
    print("0")
    return 0

def Q3(): #7568번 덩치
    n = int(input())
    HWeight = [[0, 0] for _ in range(n)] #각각 키, 몸무게, 입력 순서, 덩치 순위
    rank = [0] * n
    for i in range(n):
        HWeight[i][0], HWeight[i][1] = map(int, input().split())

    for i in range(n):
        for j in range(n):
            if HWeight[i][0] < HWeight[j][0] and HWeight[i][1] < HWeight[j][1]:
                rank[i] += 1
                

    for i in range(0, n - 1):
        print(rank[i] + 1, end = ' ')
    print(rank[n - 1] + 1, end = '')

def Q4():
    row, col = map(int, input().split())
    given = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        given[i][0:8] = input()

    board = [[0,0,0,0,0,0,0,0] for _ in range(8)]
    needToBePainted = [[10 ** 6 for _ in range(col)] for _ in range(row)]
    for i in range(row - 7):
        for j in range(col - 7):
            for k in range(8):
                board[k][0:8] = given[i +k][j:j + 8]
            
            case = [0, 0]
            #1행1열이 W인 경우
            for a in range(8):
                for b in range(8):
                    if (a + b) % 2 == 0:
                        if board[a][b] != 'W':
                            case[0] += 1
                    else:
                        if board[a][b] != 'B':
                            case[0] += 1
            #1행1열이 B인 경우
            for a in range(8):
                for b in range(8):
                    if (a + b) % 2 == 0:
                        if board[a][b] != 'B':
                            case[1] += 1
                    if (a + b) % 2 == 1:
                        if board[a][b] != 'W':
                            case[1] += 1
            needToBePainted[i][j] = min(case[0], case[1])
            case = [0, 0]
    print(min(needToBePainted)[0])
Q4()