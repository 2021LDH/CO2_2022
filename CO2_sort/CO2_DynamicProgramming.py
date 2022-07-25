#Old가 붙어있는 문제는 지난 학기에 다이나믹 프로그래밍 발표 때 풀었던 문제
def Old_Q1(): #15989번 1, 2, 3 더하기 4
    MAX = 10001
    arr = [[0,0,0,0] for _ in range(MAX)]
    arr[1][1] = 1
    arr[2][1] = 1
    arr[2][2] = 1
    arr[3][1] = 1
    arr[3][2] = 1
    arr[3][3] = 1

    for i in range(4,MAX):
        arr[i][1] = arr[i-1][1]
        arr[i][2] = arr[i-2][1] + arr[i-2][2]
        arr[i][3] = arr[i-3][1] + arr[i-3][2]+ arr[i-3][3]

    n = int(input())
    for _ in range(n):
        a = int(input())
        print(sum(arr[a]))

def Old_Q2(): #1010번 다리 놓기
    import math

    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        ans = math.factorial(b)/(math.factorial(b-a)*math.factorial(a))
        print(int(ans))

def Q1(): #24416번 알고리즘 수업 - 피보나치 수 1
    n = int(input())

    f = [0] * (n + 1)
    def fib(n):
        f[1] = f[2] = 1;
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2];  # 코드2
        return f[n]
    if n > 2: count = n - 2
    else: count = 0
    print(fib(n), count)

def Q2(): #9184번 신나는 함수 실행
    import sys
    input = sys.stdin.readline

    arr = [[[10**6 for i in range(51)] for j in range(51)] for k in range(51)]
    
    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)
        if arr[a][b][c] != 10 ** 6:
            return arr[a][b][c]
        if a < b and b < c:
            arr[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return arr[a][b][c]
        arr[a][b][c] = w(a - 1, b, c) + w(a - 1, b -1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return arr[a][b][c]
    while True:
        a, b, c = map(int,input().rstrip().split())
        if a == -1 and b == -1 and c == -1:
            break
        else:
            print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))

def Q3(): #1904번 01타일
    n = int(input())
    arr = [0] * 1000001
    arr[1], arr[2] = 1, 2
    for i in range(3, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2]) % 15746
    
    print(arr[n] % 15746)

def Q4(): #9461번 파도반 수열
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())
    m = [0] * n
    padoban = [0] * 101
    padoban[1:5] = 1, 1, 1, 2, 2
    for i in range(n):
        m[i] = int(input())

        if m[i] < 6: print(padoban[m[i]])
        else:
            for j in range(6, m[i] + 1):
                padoban[j] = padoban[j - 1] + padoban[j - 5]

            print(padoban[m[i]])
def Q5(): #1912번 연속합
    n = int(input())
    arr = list(map(int, input().split()))
    sum = [-1000*1000000] * n
    for i in range(n):
        if sum[i - 1] > 0:
            sum[i] = sum[i-1] + arr[i]
        else:
            sum[i] = arr[i]
    print(max(sum))

def Q6(): #1149번 RGB거리
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = [[0, 0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        arr[i][0:2] = map(int, input().rstrip().split())
    sum = [[0, 0, 0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        sum[i][0] = min(sum[i - 1][1], sum[i - 1][2]) + arr[i][0]
        sum[i][1] = min(sum[i - 1][0], sum[i - 1][2]) + arr[i][1]
        sum[i][2] = min(sum[i - 1][0], sum[i - 1][1]) + arr[i][2]
    print(min(sum[n][0], sum[n][1], sum[n][2]))

def Q7(): #1932번 정수 삼각형
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr[i][0:i + 1] = map(int, input().rstrip().split())

    sum = [[0 for _ in range(n)] for _ in range(n)]
    sum[0][0] = arr[0][0]
    for i in range(1, n):
        sum[i][0] = sum[i - 1][0] + arr[i][0]
        for j in range(1, n - 1):
            sum[i][j] = max(sum[i - 1][j - 1], sum[i - 1][j]) + arr[i][j]
        sum[i][n - 1] = sum[i - 1][n - 2] + arr[i][n - 1]
    print(max(sum[n - 1]))

def Q8(): #2579번 계단 오르기
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())
    if n == 1:
        print(arr[0])
    elif n == 2:
        print(arr[0] + arr[1])
    else:
        sum = [0] * n
        sum[0] = arr[0]
        sum[1] = arr[0] + arr[1]
        sum[2] = max(arr[1] + arr[2], arr[0] + arr[2])
        for i in range(3, n):
            sum[i] = max(sum[i - 3] + arr[i - 1] + arr[i], sum[i - 2] + arr[i])
        print(sum[n - 1])

def Q9(): #1463번 1로 만들기
    x = int(input())
    d = [0] * (x + 1)
    for i in range(2, x + 1):
        if i % 6 == 0:
            d[i] = min(d[i - 1] + 1, d[i // 3] + 1, d[i // 2] + 1)
        elif i % 3 != 0 and i % 2 == 0:
            d[i] = min(d[i - 1] + 1, d[i // 2] + 1)
        elif i % 3 == 0 and i % 2 != 0:
            d[i] = min(d[i - 1] + 1, d[i // 3] + 1)
        else:
            d[i] = d[i - 1] + 1
    print(d[x])

def Q10(): #10844번 쉬운 계단 수
    n = int(input())
    position = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(n + 1)]
    for i in range(1, 10):
        position[1][i] = 1
    for i in range(2, n + 1):
        position[i][0] = position[i - 1][1]
        position[i][1] = position[i - 1][0] + position[i - 1][2]
        position[i][2] = position[i - 1][1] + position[i - 1][3]
        position[i][3] = position[i - 1][2] + position[i - 1][4]
        position[i][4] = position[i - 1][3] + position[i - 1][5]
        position[i][5] = position[i - 1][4] + position[i - 1][6]
        position[i][6] = position[i - 1][5] + position[i - 1][7]
        position[i][7] = position[i - 1][6] + position[i - 1][8]
        position[i][8] = position[i - 1][7] + position[i - 1][9]
        position[i][9] = position[i - 1][8]
    print(sum(position[n]) % 1000000000)
Q10()