def Q1(): #5086번 배수와 약수
    import sys

    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if a + b == 0:
            break
        if a % b == 0:
            print('multiple')
        elif b % a == 0:
            print('factor')
        else: print('neither')

def Q2(): #1037번 약수
    a = int(input())
    b = list(map(int, input().split()))
    max = max(b)
    min = min(b)
    print(max * min)

def Q3(): #2609번 최대공약수와 최소공배수
    import math

    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y / gcd(x, y)

    a, b = map(int, input().split())
    print(math.gcd(a, b))
    print(math.lcm(a, b))

def Q4(): #1934번 최소공배수
    import math, sys

    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(math.lcm(a, b))

def Q5(): #1934번 최소공배수
    import math, sys

    n = int(sys.stdin.readline().rstrip())
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline().rstrip()))
    
    interval = []
    for i in range(1, n):
        interval.append(arr[i] - arr[i - 1])

    temp = interval[0]
    for i in range(1, n - 1):
        temp = math.gcd(temp, interval[i])

    answer = set()
    answer.add(temp)
    for i in range(2, int(temp**0.5 + 1)):
        if temp % i == 0:
            answer.add(i)
            answer.add(temp // i)
    answer = list(answer)
    answer.sort()
    print(*answer)

def Q6(): #3036번 링
    import math

    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        print(arr[0] // math.gcd(arr[0], arr[i]), end = '')
        print('/', end = '')
        print(arr[i] // math.gcd(arr[0], arr[i]))

def Q7(): #11050번 이항 계수 1
    import math
    a, b = map(int, input().split())
    print(math.factorial(a) // (math.factorial(b) * math.factorial(a - b)))

def Q8(): #11051번 이항 계수 2
    import math
    a, b = map(int, input().split())
    print((math.factorial(a) // (math.factorial(b) * math.factorial(a - b))) % 10007)

#9번 #1010번 다리 놓기는 전에 다이나믹 프로그래밍에 있던 문제이므로 제외

def Q10(): #9375번 패션왕 신해빈
    t = int(input())

    for i in range(t):
        n = int(input())
        clothes = {}
        for j in range(n):
            temp = list(input().split())
            if temp[1] in clothes:
                clothes[temp[1]].append(temp[0])
            else:
                clothes[temp[1]] = [temp[0]]

        cnt = 1

        for i in clothes:
            cnt *= (len(clothes[i])+1)
        print(cnt-1)

def Q11():
    import math
    
    a = math.factorial(int(input()))
    count = 0
    while True:
        if a % 10 == 0:
            count += 1
            a = a // 10
        else: break
    print(count)

def Q12():
    import math

    a, b = map(int, input().split())
    countTwo, countFive = 0, 0

    def countTwo(n):
        count = 0
        while n != 0:
            n = n // 2
            count += n
        return count

    def countFive(n):
        count = 0
        while n != 0:
            n = n // 5
            count += n
        return count
    print(min(countTwo(a) - countTwo(b) - countTwo(a - b), countFive(a) - countFive(b) - countFive(a - b)))
Q10()