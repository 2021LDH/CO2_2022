def Q1(): #11047번 동전 0
    n, k = map(int,input().split())
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())
    
    a = 0
    for i in range(n):
        a += k // arr[-(i + 1)]
        k %= arr[-(i + 1)]
    print(a)

def Q2(): #1931번 회의실 배정
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key = lambda x: (x[1], x[0]))
    sum = 0
    end = 0
    for a, b in arr:
        if a >= end:
            sum += 1
            end = b
    print(sum)

def Q3(): #11399번 ATM
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    sum = 0
    for i in range(n):
        sum += arr[i] * (n - i)
    print(sum)

def Q4(): #1541번 잃어버린 괄호
    str = input()

    num = [0] * 25
    start = 0
    a = 0
    b = 0
    for i in range(len(str)):
        if str[i] == "+" or str[i] == "-":
            num[a] = int(str[start:i])
            start = i + 1
            if b == 1:
                num[a] = (-1) * num[a]
            if str[i] == "-":
                b = 1
            a += 1
    num[a] = int(str[start:len(str)])
    if b == 1:
        num[a] = (-1) * num[a]
    result = 0
    for i in range(25):
        result += num[i]
    print(result)

def Q5(): #13305번 주유소
    n = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))

    result = 0
    m = price[0]
    for i in range(n-1):
        if price[i] < m:
            m = price[i]
        result += m * distance[i]
    
    print(result)
Q5()