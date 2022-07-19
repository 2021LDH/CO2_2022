def Q1(): #10872번 팩토리얼
    a = int(input())
    def factorial(a):
        if(a == 0 or a == 1):   return 1
        return a * factorial(a - 1)
    print(factorial(a))

def Q2(): #10870번 피보나치 수 5
    a = int(input())
    fibo = [0] * 21
    fibo[0], fibo[1] = 0, 1
    for i in range(2, a + 1):
        fibo[i] = fibo[i - 2] + fibo[i - 1]
    print(fibo[a])

def Q3(): #17478번 재귀함수가 뭔가요?
    a = int(input())
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    print("\"재귀함수가 뭔가요?\"")
    print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    print("____\"재귀함수가 뭔가요?\"")
    for j in range(1, a):
        for i in range(j):
            print("____", end="")
        print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        for i in range(j):
            print("____", end="")
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        for i in range(j):
            print("____", end="")
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        for i in range(j + 1):
            print("____", end="")
        print("\"재귀함수가 뭔가요?\"")
    for i in range(0, a):
        print("____", end="")
    print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    for j in range(0, a):
        for i in range(j, a):
            print("____", end="")
        print("라고 답변하였지.")
    print("라고 답변하였지.")

def Q4(): #2447번 별 찍기 - 10
    import sys
    sys.setrecursionlimit(10 ** 6)
    import math
    a = int(input())
    k = int(math.log(a, 3))

    b = a
    x, y = a, a;
    basic = [[0] * 3 for _ in range(3)]
    result = [['*'] * (3 ** 8) for _ in range(3 ** 8)]

    def printResult(result):
        for i in range(a):
            for j in range(a):
                print(result[i][j], end = '')
            print()

    def deleteStar(x, y):
        for i in range(x // 3, (x // 3) * 2):
                for j in range(y // 3, (y // 3) * 2):
                    result[i][j] = ' '

    def copyStar(x, y):
        for i in range(0, x // 3):
            result[x // 3 + i][0:y // 3] = result[i][0:y // 3]
            result[(x // 3) * 2 + i][0:y // 3] = result[i][0:y // 3]
            result[0 + i][y // 3:(y // 3) * 2] = result[i][0:y // 3]
            result[(x // 3) * 2 + i][y // 3:(y // 3) * 2] = result[i][0:y // 3]
            result[0 + i][(y // 3) * 2:y] = result[i][0:y // 3]
            result[x // 3 + i][(y // 3) * 2:y] = result[i][0:y // 3]
            result[(x // 3) * 2 + i][(y // 3) * 2:y] = result[i][0:y // 3]

    def iteration(x, y):
        if x >= 3 and y >= 3:
            deleteStar(x, y)
            iteration(x // 3, y // 3)

    iteration(x, y)
    x, y = a, a;
    if a != 3:
        for i in range(1, k + 2):
            copyStar(3 ** i, 3 ** i)
    printResult(result)

def Q5(): #11729번 하노이 탑 이동 순서
    n = int(input())

    def hanoi(n, a, b, c):
        if n == 1:
            print(a, c)
        else:
            hanoi(n - 1, a, c, b)
            print(a, c)
            hanoi(n - 1, b, a, c)
    print(2 ** n - 1)
    hanoi(n, 1, 2, 3)